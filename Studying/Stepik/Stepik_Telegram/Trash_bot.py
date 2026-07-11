import asyncio
import aiosqlite
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
DB_PATH = "trash_report.db"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# --- Работа с БД ---
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS trash_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                answer TEXT NOT NULL,
                report_date TEXT NOT NULL
            )
        """)
        await db.execute("CREATE INDEX IF NOT EXISTS idx_trash_user_date ON trash_reports(user_id, report_date)")
        await db.commit()

def get_iso_week_and_year(date_str: str):
    """Возвращает (year, week) для даты в формате YYYY-MM-DD"""
    d = datetime.strptime(date_str, "%d-%m-%Y")
    year, week, _ = d.isocalendar()
    print(year,week)
    return year, week

async def save_or_update_report(user_id: int, answer: str):
    today = datetime.now().strftime("%d-%m-%Y")
    async with aiosqlite.connect(DB_PATH) as db:
        # Пробуем обновить запись за сегодня
        cursor = await db.execute(
            """
            UPDATE trash_reports
            SET answer = ?, report_date = ?
            WHERE user_id = ? AND report_date = ?
            """,
            (answer, today, user_id, today)
        )
        if cursor.rowcount > 0:
            await db.commit()
            return "updated", today

        # Если нет записи за сегодня — вставляем новую
        await db.execute(
            "INSERT INTO trash_reports (user_id, answer, report_date) VALUES (?, ?, ?)",
            (user_id, answer, today)
        )
        await db.commit()
        return "inserted", today


def format_date_to_day_month(date_str: str) -> str:
    """
    Принимает дату в формате 'YYYY-MM-DD' и возвращает строку вида 'Номер дня Название месяца'.
    Например: '5 июля'
    """
    # Парсим строку в объект datetime
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")

    # Словарь для перевода названий месяцев на русский
    months_ru = {
        1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля",
        5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
        9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"
    }

    day = date_obj.day
    month_name = months_ru[date_obj.month]

    return f"{day} {month_name}"

async def get_last_report_for_user(user_id: int):
    """Получает последнюю запись пользователя (по id DESC)"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT id, answer, report_date FROM trash_reports WHERE user_id = ? ORDER BY id DESC LIMIT 1",
            (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return {"id": row[0], "answer": row[1], "report_date": row[2]}
    return None

async def can_edit_this_week(record_date: str) -> bool:
    """Проверяет, что record_date и сегодня находятся в одной календарной неделе"""
    rec_year, rec_week = get_iso_week_and_year(record_date)
    now = datetime.now()
    cur_year, cur_week, _ = now.isocalendar()
    return (rec_year == cur_year) and (rec_week == cur_week)

async def update_report_if_allowed(user_id: int, new_answer: str) -> tuple[bool, str]:
    record = await get_last_report_for_user(user_id)
    if not record:
        return False, "Нет предыдущих записей для редактирования."

    if not await can_edit_this_week(record["report_date"]):
        return False, f"Нельзя изменить запись от {record['report_date']}: она старше текущей недели."

    # Обновляем именно эту запись (по id)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE trash_reports SET answer = ? WHERE id = ?",
            (new_answer, record["id"])
        )
        await db.commit()
    return True, f"Статус изменён на «{new_answer}» для записи от {record['report_date']}."

# --- Клавиатуры ---
def get_start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Сообщить о сборе мусора")
    return builder.as_markup(resize_keyboard=True)

def get_yes_no_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Да, собран")
    builder.button(text="Нет, не собран")
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def get_edit_keyboard() -> InlineKeyboardMarkup:
    edit_button = InlineKeyboardButton(
        text='Изменить ответ',
        callback_data='edit_button'
    )
    edit_keyboard = InlineKeyboardMarkup(inline_keyboard=[[edit_button]])
    return edit_keyboard

# --- Функция рассылки (опрос по расписанию) ---
async def send_weekly_poll():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT DISTINCT user_id FROM trash_reports") as cursor:
            rows = await cursor.fetchall()

    if not rows:
        return

    for (user_id,) in rows:
        try:
            await bot.send_message(
                chat_id=user_id,
                text="Напоминаем: пожалуйста, сообщите, собран ли мусор сегодня.",
                reply_markup=get_yes_no_keyboard()
            )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

# --- Обработчики ---
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для отчёта о сборе мусора.\nНажмите кнопку ниже, чтобы сообщить статус.",
        reply_markup=get_start_keyboard()
    )

@dp.message(F.text == "Сообщить о сборе мусора")
async def ask_trash_status(message: types.Message):
    await message.answer(
        "Мусор собран?",
        reply_markup=get_yes_no_keyboard()
    )

@dp.message(F.text.in_({"Да, собран", "Нет, не собран"}))
async def handle_answer(message: types.Message):
    answer_map = {
        "Да, собран": "Yes",
        "Нет, не собран": "No"
    }
    answer = answer_map[message.text]

    result, date_used = await save_or_update_report(message.from_user.id, answer)

    day_month = format_date_to_day_month(date_used)

    status_text = "изменён" if result == "updated" else "сохранён"
    await message.answer(
        f"Спасибо, статус «{message.text}» {status_text} на {day_month}.",
        reply_markup=get_edit_keyboard()
    )

@dp.callback_query(F.data == 'edit_button')
async def process_button_edit_click(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    # Сначала проверяем, можно ли редактировать
    record = await get_last_report_for_user(user_id)
    if not record:
        await callback.message.answer("Нет записей для редактирования.")
        return

    if not await can_edit_this_week(record["report_date"]):
        await callback.message.answer(
            f"❌ Нельзя изменить запись от {record['report_date']}: "
            f"она старше текущей недели (можно менять только в пределах одной календарной недели)."
        )
        return

    # Показываем вопрос для выбора нового статуса
    await callback.message.answer(
        "Выберите новый статус:",
        reply_markup=get_yes_no_keyboard()
    )

# Отдельный обработчик, который реально обновляет запись при выборе Да/Нет в режиме редактирования
@dp.message(F.text.in_({"Да, собран", "Нет, не собран"}))
async def handle_edit_answer(message: types.Message):
    # Проверяем, что это именно редактирование (можно отличать по контексту, но для простоты — по наличию последней записи)
    user_id = message.from_user.id
    record = await get_last_report_for_user(user_id)

    # Если нет последней записи или она уже не в текущей неделе — считаем это обычным ответом, а не редактированием
    if not record or not await can_edit_this_week(record["report_date"]):
        # Это обычный новый ответ на сегодня (или неделя уже другая, тогда создаётся новая запись)
        answer_map = {"Да, собран": "Yes", "Нет, не собран": "No"}
        answer = answer_map[message.text]
        result, date_used = await save_or_update_report(user_id, answer)
        status_text = "изменён" if result == "updated" else "сохранён"
        await message.answer(
            f"Статус «{message.text}» {status_text} на {date_used}.",
            reply_markup=get_edit_keyboard()
        )
        return

    # Иначе — это редактирование существующей записи
    answer_map = {"Да, собран": "Yes", "Нет, не собран": "No"}
    new_answer = answer_map[message.text]
    ok, text = await update_report_if_allowed(user_id, new_answer)
    if ok:
        await message.answer(f"{text}\nТеперь статус обновлён.", reply_markup=get_edit_keyboard())
    else:
        await message.answer(text)

# --- Запуск ---
async def main():
    await init_db()

    scheduler.add_job(
        send_weekly_poll,
        trigger=CronTrigger(day_of_week='mon', hour=16, minute=0),
        id='weekly_trash_poll',
        replace_existing=True
    )
    scheduler.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

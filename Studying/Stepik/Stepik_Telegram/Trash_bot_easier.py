
import asyncio
import aiosqlite
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardMarkup, InlineKeyboardBuilder,ReplyKeyboardBuilder
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


streets_list = [
        "Пер. Коммунальный",
        "Пер. Нефтяников",
        "Пер. Степной",
        "Ул. Войкова",
        "Ул. Гай",
        "Ул. Дачная",
        "Ул. Жукова",
        "Ул. Коминтерна",
        "Ул. Красноармейская",
        "Ул. Лабинская",
        "Ул. Марата",
        "Ул. Международная",
        "Ул. Мира",
        "Ул. Революционная",
        "Ул. Старателей",
        "Ул. Степная",
        "Ул. Телеграфная",
        "Ул. Чапаева"
    ]

# --- Работа с БД ---
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS trash_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                street TEXT NOT NULL,
                house_number INTEGER NOT NULL,
                answer TEXT NOT NULL,
                report_date TEXT NOT NULL
            )
        """)
        await db.commit()



def get_today_str() -> str:
    """Возвращает сегодняшнюю дату в формате YYYY-MM-DD"""
    return datetime.now().strftime("%Y-%m-%d")

def get_iso_week(date_str: str) -> tuple[int, int]:
    """Безопасное получение года и номера недели"""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.isocalendar()[:2]  # (year, week)
    except Exception:
        # Если дата битая — возвращаем заведомо несовпадающие значения
        return (0, 0)

def format_day_month(date_str: str) -> str:
    """Преобразует YYYY-MM-DD в '10 июля'"""
    d = datetime.strptime(date_str, "%Y-%m-%d")
    months = [
        "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
        "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"
    ]
    return f"{d.day} {months[d.month - 1]}"

async def save_or_update_report(user_id: int, answer: str):
    today = get_today_str()
    async with aiosqlite.connect(DB_PATH) as db:
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

        await db.execute(
            "INSERT INTO trash_reports (user_id, answer, report_date) VALUES (?, ?, ?)",
            (user_id, answer, today)
        )
        await db.commit()
        return "inserted", today

async def get_last_report(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT id, answer, report_date FROM trash_reports WHERE user_id = ? ORDER BY id DESC LIMIT 1",
            (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return {"id": row[0], "answer": row[1], "report_date": row[2]}
    return None

async def can_edit_record(record_date: str) -> bool:
    rec_year, rec_week = get_iso_week(record_date)
    cur_year, cur_week, _ = datetime.now().isocalendar()
    return rec_year == cur_year and rec_week == cur_week

async def update_record_by_id(record_id: int, new_answer: str) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE trash_reports SET answer = ? WHERE id = ?",
            (new_answer, record_id)
        )
        await db.commit()
    return True

# --- Клавиатуры ---


def get_start_kb():
    btn= KeyboardButton(text="Сообщить о сборе мусора",callback_data='answer_button')
    return ReplyKeyboardMarkup(keyboard=[[btn]],resize_keyboard=True)

def get_yes_no_kb():
    btn_yes = KeyboardButton(text="Да")
    btn_no = KeyboardButton(text="Нет")
    return ReplyKeyboardMarkup(keyboard=[[btn_yes,btn_no]],resize_keyboard=True)

def get_yes_no_trash_kb():
    btn_yes = KeyboardButton(text="Да, собран")
    btn_no = KeyboardButton(text="Нет, не собран")
    return ReplyKeyboardMarkup(keyboard=[[btn_yes,btn_no]],resize_keyboard=True)

def get_edit_kb():
    btn = InlineKeyboardButton(text="Изменить ответ", callback_data="edit_button")
    return InlineKeyboardMarkup(inline_keyboard=[[btn]])

def get_streets_kb():

    builder = ReplyKeyboardBuilder()
    for street_name in streets_list:
        builder.add(KeyboardButton(text=street_name))
    builder.adjust(1)
    return builder.as_markup()


# --- Рассылка ---
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
                reply_markup=get_yes_no_trash_kb()
            )
        except Exception as e:
            print(f"Не удалось отправить пользователю {user_id}: {e}")

# --- Обработчики ---
@dp.message(CommandStart())
async def cmd_start(msg):
    await msg.answer(
        "Привет! Я бот для отчёта о сборе мусора.\nВыберите вашу улицу.",
        reply_markup=get_streets_kb()
    )

@dp.message(F.text.in_(streets_list))
async def cmd_start(msg):
    await msg.answer(
        f"Ваша улица: {msg.text}.\nВерно?",
        reply_markup=get_yes_no_kb()
    )

@dp.message(F.text.in_(['Нет','Да']))
async def cmd_start(msg):
    if msg.text == 'Нет':
        await msg.answer(
            f"Выберите вашу улицу:",
            reply_markup=get_streets_kb()
        )
    else:
        await msg.answer(
            f"Ваша улица: {msg.text}.",
            reply_markup=ReplyKeyboardRemove()
        )


@dp.message(F.text == "Сообщить о сборе мусора")
async def ask_status(msg):
    await msg.answer("Мусор собран?", reply_markup=get_yes_no_trash_kb())

@dp.callback_query(F.data == "edit_button")
async def cb_edit(callback):
    await callback.answer()
    user_id = callback.from_user.id
    record = await get_last_report(user_id)

    if not record:
        await callback.message.answer("Нет записей для редактирования.")
        return

    if not await can_edit_record(record["report_date"]):
        dm = format_day_month(record["report_date"])
        await callback.message.answer(f"❌ Нельзя изменить запись от {dm}: она старше текущей недели.")
        return

    # Показываем кнопки для выбора нового статуса
    await callback.message.answer(
        f"Текущая запись от {format_day_month(record['report_date'])}: «{record['answer']}».\nВыберите новый статус:",
        reply_markup=get_yes_no_trash_kb()
    )

@dp.message(F.text.in_({"Да, собран", "Нет, не собран"}))
async def handle_yes_no(msg):
    user_id = msg.from_user.id
    answer_map = {"Да, собран": "Да", "Нет, не собран": "Нет"}
    new_answer = answer_map[msg.text]

    last = await get_last_report(user_id)
    today = get_today_str()

    # Логика: если есть последняя запись и она за СЕГОДНЯ — это просто обновление статуса за сегодня
    if last and last["report_date"] == today:
        # Обычный случай: обновляем запись за сегодня
        await save_or_update_report(user_id, new_answer)
        day_month = format_day_month(today)
        status_text = "изменён"
        await msg.answer(
            f"Спасибо, статус «{msg.text}» {status_text} на {day_month}.",
            reply_markup=get_edit_kb()
        )
        return

    # Если есть запись, но НЕ за сегодня, и она в пределах недели — считаем, что пользователь хочет её отредактировать
    if last and await can_edit_record(last["report_date"]):
        success = await update_record_by_id(last["id"], new_answer)
        if success:
            day_month = format_day_month(last["report_date"])
            await msg.answer(
                f"Статус изменён на «{msg.text}» для записи от {day_month}.\nТеперь статус обновлён.",
                reply_markup=get_edit_kb()
            )
        else:
            await msg.answer("Не удалось обновить запись.")
        return

    # Иначе — это новая запись (не сегодня и не в пределах недели для редактирования)
    result, date_used = await save_or_update_report(user_id, new_answer)
    status_text = "изменён" if result == "updated" else "сохранён"
    day_month = format_day_month(date_used)
    await msg.answer(
        f"Статус «{msg.text}» {status_text} на {day_month}.",
        reply_markup=get_edit_kb()
    )

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
import os
import asyncio
import aiosqlite
from aiogram import BaseMiddleware
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message, \
    CallbackQuery, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timedelta

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class GlobalMessageLoggerMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        # Проверяем, что событие - это сообщение
        if isinstance(event, Message):
            user_id = event.from_user.id
            text = event.text or "[Нет текста (фото/команда)]"

            # Получаем текущее состояние из контекста (data)
            # В aiogram 3 состояние хранится в data['state']
            current_state = data.get("state")

            # Формируем лог
            log_msg = f'Сообщение от {event.from_user.full_name}\nid: {user_id}\nтекст: {text}'
            logger.info(f"[GUARD] {log_msg}")

            if ADMINS_IDS:
                try:
                    # if user_id != ADMINS_IDS[0]:
                    await bot.send_message(
                        chat_id = ADMINS_IDS[0],
                        text= log_msg
                    )
                except Exception as e:
                    logger.error(f"Не удалось отправить уведомление админу: {e}")

        # Передаем управление дальше (следующему middleware или хендлеру)
        return await handler(event, data)


def get_week_range_text(date_str: str) -> str:
    """
    Возвращает строку вида '15 Июля — 21 Июля' для недели,
    к которой относится переданная дата (YYYY-MM-DD).
    """
    d = datetime.strptime(date_str, "%Y-%m-%d")
    year, week, weekday = d.isocalendar()  # weekday: 1=Пн, ..., 7=Вс

    # Находим понедельник этой недели
    monday = d - timedelta(days=weekday - 1)
    # Находим воскресенье этой недели
    sunday = monday + timedelta(days=6)

    months = [
        "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
        "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"
    ]

    def fmt(dt):
        return f"{dt.day} {months[dt.month - 1]}"

    return f"{fmt(monday)} — {fmt(sunday)}"




# --- Конфигурация ---
BOT_TOKEN = os.getenv('BOT_TOKEN_ripe_owl_bot')
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в окружении")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

DB_PATH = "trash_report.db"


# --- ВАЖНО: Подключаем middleware здесь ---
dp.message.middleware(GlobalMessageLoggerMiddleware())
# -------------------------------------------
scheduler = AsyncIOScheduler()

# --- Константы и утилиты ---
RUSSIAN_LETTERS = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
ADMINS_IDS = [852757379]
CONTACTS = ['+7 918 414 78 32']

def is_russian_only_no_regex(text: str) -> bool:
    if not text:
        return False
    return all(ch in RUSSIAN_LETTERS for ch in text)


streets_list = [
    "Пер. Коммунальный", "Пер. Нефтяников", "Пер. Степной", "Ул. Войкова",
    "Ул. Гай", "Ул. Дачная", "Ул. Жукова", "Ул. Коминтерна",
    "Ул. Красноармейская", "Ул. Лабинская", "Ул. Марата", "Ул. Международная",
    "Ул. Мира", "Ул. Революционная", "Ул. Старателей", "Ул. Степная",
    "Ул. Телеграфная", "Ул. Чапаева"
]

kostroma_streets = ["Ул. Индустриальная","д.Самково","Ул. Свердлова"]

streets_list += kostroma_streets

class FSMFillForm(StatesGroup):
    fill_street = State()
    street_confirming = State()
    fill_house_number = State()
    house_number_confirming = State()



def get_today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def get_iso_week(date_str: str) -> tuple[int, int]:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.isocalendar()[:2]
    except Exception:
        return (0, 0)


def format_day_month(date_str: str) -> str:
    d = datetime.strptime(date_str, "%Y-%m-%d")
    months = [
        "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
        "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"
    ]
    return f"{d.day} {months[d.month - 1]}"


# --- Работа с БД ---

async def init_db():

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS trash_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                user_name TEXT NOT NULL,
                street TEXT NOT NULL,
                house_number TEXT NOT NULL,
                answer TEXT,
                report_date TEXT NOT NULL,
                iso_year INTEGER,
                iso_week INTEGER
            )
        """)


        # Уникальный индекс: один отчёт на пользователя в ISO‑неделю
        await db.execute("""
                    CREATE UNIQUE INDEX IF NOT EXISTS idx_user_iso_week
                    ON trash_reports (user_id, iso_year, iso_week)
                """)

        logger.info(f"[DATABASE], состояние: Создана или подгружена")
        await db.commit()


async def register_user(user_id: int, name: str, street: str, house_number: str):
    today = get_today_str()
    iso_year, iso_week = get_iso_week(today)

    async with aiosqlite.connect(DB_PATH) as db:
        # 1. Сначала проверяем: а есть ли вообще этот пользователь в базе?
        cursor_user = await db.execute(
            "SELECT 1 FROM trash_reports WHERE user_id = ? LIMIT 1",
            (user_id,)
        )
        user_exists = await cursor_user.fetchone() is not None

        if user_exists:
            # Пользователь уже есть. Значит, адрес за ним уже закреплён.
            # Возвращаем успех, ничего не вставляя.
            return True

        # 2. Если пользователя нет, проверяем, не занят ли адрес кем-то другим
        cursor_addr = await db.execute(
            "SELECT user_id FROM trash_reports WHERE street = ? AND house_number = ?",
            (street, house_number)
        )
        addr_exists = await cursor_addr.fetchone()

        if addr_exists:
            # Адрес занят другим пользователем
            return False

        # 3. Если пользователь новый и адрес свободен — вставляем первую запись
        await db.execute(
            """
            INSERT INTO trash_reports
            (user_id, user_name, street, house_number, answer, report_date, iso_year, iso_week)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, name, street, house_number, None, today, iso_year, iso_week),
        )
        await db.commit()
        return True


async def save_or_update_report(user_id: int, answer: str):
    today = get_today_str()
    year, week = get_iso_week(today)

    async with aiosqlite.connect(DB_PATH) as db:
        # Ищем запись за эту ISO‑неделю
        cursor = await db.execute(
            """
            SELECT id, user_name, street, house_number
            FROM trash_reports
            WHERE user_id = ? AND iso_year = ? AND iso_week = ?
            """,
            (user_id, year, week),  # <-- передаём int, без str() и zfill
        )
        row = await cursor.fetchone()

        if row:
            # Запись за эту неделю уже есть → обновляем ответ
            record_id, name, street, house_number = row
            await db.execute(
                "UPDATE trash_reports SET answer = ? WHERE id = ?",
                (answer, record_id)
            )
            await db.commit()
            return "updated", today

        # Записи за эту неделю нет → создаём новую
        cur = await db.execute(
            "SELECT user_name, street, house_number FROM trash_reports WHERE user_id = ? ORDER BY id DESC LIMIT 1",
            (user_id,)
        )
        addr_row = await cur.fetchone()

        if not addr_row:
            raise ValueError("Пользователь не зарегистрирован")

        name, street, house_number = addr_row

        await db.execute(
            """
            INSERT INTO trash_reports
            (user_id, user_name, street, house_number, answer, report_date, iso_year, iso_week)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, name, street, house_number, answer, today, year, week),  # <-- добавили year, week
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
    btn = KeyboardButton(text="Сообщить о сборе мусора")
    return ReplyKeyboardMarkup(keyboard=[[btn]], resize_keyboard=True)


def get_yes_no_kb():
    btn_yes = KeyboardButton(text="Да")
    btn_no = KeyboardButton(text="Нет")
    return ReplyKeyboardMarkup(keyboard=[[btn_yes, btn_no]], resize_keyboard=True)


def get_yes_no_trash_kb():
    btn_yes = KeyboardButton(text="Да, собран")
    btn_no = KeyboardButton(text="Нет, не собран")
    return ReplyKeyboardMarkup(keyboard=[[btn_yes, btn_no]], resize_keyboard=True,one_time_keyboard=True)


def get_edit_kb():
    btn = InlineKeyboardButton(text="Изменить ответ", callback_data="edit_button")
    return InlineKeyboardMarkup(inline_keyboard=[[btn]])


def get_streets_kb():
    builder = ReplyKeyboardBuilder()
    for street_name in streets_list:
        builder.add(KeyboardButton(text=street_name))
    builder.adjust(1)
    return builder.as_markup()


def get_house_number_kb():
    builder = ReplyKeyboardBuilder()
    for house_number in range(1, 101):
        builder.add(KeyboardButton(text=str(house_number)))
    builder.adjust(1)
    return builder.as_markup()


def get_report_kb(user_id):
    btn_report = KeyboardButton(text='Сообщить о сборе мусора')

    return ReplyKeyboardMarkup(keyboard=[[btn_report]], resize_keyboard=True)



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
                text="Напоминаем: пожалуйста, сообщите, собран ли мусор на этой неделе.",
                reply_markup=get_yes_no_trash_kb()
            )
        except Exception as e:
            print(f"Не удалось отправить пользователю {user_id}: {e}")


# --- Обработчики ---


@dp.message(F.text=='/stat')
async def admin_stat_global(msg:Message):
    if msg.from_user.id not in ADMINS_IDS:
        await msg.answer('❌ Доступ запрещён.')
        return

    await get_statistic(msg)

@dp.message(F.text.in_(streets_list), StateFilter(FSMFillForm.fill_street))
async def fill_street_process(msg: Message, state: FSMContext):
    await state.update_data(street=msg.text)
    await msg.answer(
        f"Ваша улица: {msg.text}.\nВерно?",
        reply_markup=get_yes_no_kb()
    )
    await state.set_state(FSMFillForm.street_confirming)


@dp.message(StateFilter(FSMFillForm.fill_street))
async def other_fill_street(msg: Message, state: FSMContext):
    await msg.answer(
        text='Мы сейчас выбираем улицу.\nВыберите вашу улицу из списка:',
        reply_markup=get_streets_kb()
    )


@dp.message(F.text == 'Нет', StateFilter(FSMFillForm.street_confirming))
async def restart_fill_street_process(msg: Message, state: FSMContext):
    await msg.answer("Выберите вашу улицу:", reply_markup=get_streets_kb())
    await state.set_state(FSMFillForm.fill_street)


@dp.message(F.text == 'Да', StateFilter(FSMFillForm.street_confirming))
async def confirm_fill_street_process(msg: Message, state: FSMContext):
    data = await state.get_data()
    street = data["street"]
    await msg.answer(
        f"Ваша улица: {street}.\nВыберите номер дома:",
        reply_markup=get_house_number_kb()
    )
    await state.set_state(FSMFillForm.fill_house_number)


@dp.message(StateFilter(FSMFillForm.street_confirming))
async def other_confirm_street(msg: Message, state: FSMContext):
    data = await state.get_data()
    street = data["street"]
    await msg.answer(
        f"Пожалуйста, нажмите «Да» или «Нет», чтобы подтвердить улицу.\nВаша улица: {street}.\nВерно?",
        reply_markup=get_yes_no_kb()
    )


@dp.message(F.text.isdigit(), StateFilter(FSMFillForm.fill_house_number))
async def confirm_house_number(msg: Message, state: FSMContext):
    await state.update_data(house_number=msg.text)
    await msg.answer(
        f"Номер вашего дома : {msg.text}. Верно?",
        reply_markup=get_yes_no_kb()
    )
    await state.set_state(FSMFillForm.house_number_confirming)


@dp.message(StateFilter(FSMFillForm.fill_house_number))
async def other_confirm_house_number(msg: Message, state: FSMContext):
    await msg.answer(
        "Выберите номер дома (цифрами):",
        reply_markup=get_house_number_kb()
    )
    await state.set_state(FSMFillForm.fill_house_number)


@dp.message(F.text == 'Нет', StateFilter(FSMFillForm.house_number_confirming))
async def restart_fill_house_number_process(msg: Message, state: FSMContext):
    await state.update_data(house_number=None)
    await msg.answer(
        "Выберите номер дома:",
        reply_markup=get_house_number_kb()
    )
    await state.set_state(FSMFillForm.fill_house_number)


@dp.message(F.text == 'Да', StateFilter(FSMFillForm.house_number_confirming))
async def confirm_house_number_process(msg: Message, state: FSMContext):
    data = await state.get_data()
    house_number = data['house_number']
    name = data['name']
    street = data['street']
    user_id = msg.from_user.id

    await msg.answer(
        text=f"Благодарю! Ваша анкета:\n\n"
             f"Имя: {name}\n"
             f"Адрес: {street} {house_number}",
        reply_markup=ReplyKeyboardRemove()
    )


    if await register_user(
        user_id=user_id,
        name=name,
        street=street,
        house_number=house_number
    ):
        await state.clear()
        await msg.answer("Теперь вы можете сообщать о сборе мусора при опросе или по кнопке.",reply_markup=get_report_kb())
    else:
        await state.clear()
        await state.set_state(FSMFillForm.fill_street)
        await msg.answer(
            "Такой адрес уже есть в базе. Пожалуйста, выберите другой адрес или уточните номер дома.",
            reply_markup=get_streets_kb()  # твоя клавиатура со списком улиц
        )



@dp.message(StateFilter(FSMFillForm.house_number_confirming))
async def other_house_number_confirmation(msg: Message, state: FSMContext):
    data = await state.get_data()
    house_number = data['house_number']
    await msg.answer(
        f"Пожалуйста, нажмите «Да» или «Нет», чтобы подтвердить номер дома.\nНомер вашего дома : {house_number}. Верно?",
        reply_markup=get_yes_no_kb()
    )


@dp.message(F.text == "Сообщить о сборе мусора")
async def ask_status(msg: Message):
    await msg.answer("Мусор собран?", reply_markup=get_yes_no_trash_kb())


@dp.callback_query(F.data == "edit_button")
async def cb_edit(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    record = await get_last_report(user_id)

    if not record:
        await callback.message.answer("Нет записей для редактирования.")
        return

    if not await can_edit_record(record["report_date"]):
        week_range = get_week_range_text(record["report_date"])
        await callback.message.answer(
            f"❌ Нельзя изменить запись за неделю {week_range}: она старше текущей календарной недели."
        )
        return

    week_range = get_week_range_text(record["report_date"])
    await callback.message.answer(
        f"Текущая запись за неделю {week_range}: «{record['answer']}».\nВыберите новый статус:",
        reply_markup=get_yes_no_trash_kb()
    )


@dp.message(F.text.in_({"Да, собран", "Нет, не собран"}))
async def handle_yes_no(msg: Message):
    user_id = msg.from_user.id
    answer_map = {"Да, собран": "Да", "Нет, не собран": "Нет"}
    new_answer = answer_map[msg.text]

    result, _ = await save_or_update_report(user_id, new_answer)

    # Получаем актуальную запись, чтобы взять её report_date
    record = await get_last_report(user_id)
    if not record:
        await msg.answer("Не удалось найти запись.")
        return

    week_range = get_week_range_text(record["report_date"])

    if result == "updated":
        await msg.answer(
            f"Статус за неделю {week_range} обновлён на: «{new_answer}».",
            reply_markup=get_edit_kb()
        )
    else:
        await msg.answer(f"Записана новая отметка за неделю {week_range}: «{new_answer}».",reply_markup=get_edit_kb())


@dp.message(F.text == 'Получить статистику за эту неделю')
async def get_statistic(msg:Message):

    today = get_today_str()
    iso_year, iso_week = get_iso_week(today)

    async with aiosqlite.connect(DB_PATH) as db:

        cursor = await  db.execute(f"""
                            SELECT user_id,user_name,street,house_number,answer,report_date FROM trash_reports
                            WHERE iso_year=? AND iso_week=? """,
                         (iso_year,iso_week,)

                        )
        rows = await cursor.fetchall()
        text = ''
        for row in rows:
            user_id,user_name,street,house_number,answer,report_date = row
            text += (f"Пользователь: {user_name}\n"
                f"Адрес: {street} {house_number}\n"
                f"Дата: {report_date}\n"
                f"Ответ: {answer}\n\n"
                )

        await msg.answer(
            text=text
        )

@dp.message()
async def unregistered_guard(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    current_state = await state.get_state()

    # Сначала проверяем БД
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT 1 FROM trash_reports WHERE user_id = ?",
            (user_id,)
        )
        exists = await cursor.fetchone()

    if not exists:
        # Пользователь НЕ зарегистрирован: запускаем регистрацию
        logger.info(f"[GUARD] Пользователь {user_id} НЕ найден → регистрация")
        await state.update_data(name=msg.from_user.full_name)
        await msg.answer(
            f"Привет, {msg.from_user.full_name}! Сначала укажите адрес.\nВыберите улицу:",
            reply_markup=get_streets_kb()
        )
        await state.set_state(FSMFillForm.fill_street)
        return  # Важно: дальше не идём

    # Пользователь зарегистрирован: показываем главное меню и прерываем
    logger.info(f"[GUARD] Пользователь {user_id} найден → показываем меню")
    await msg.answer(
        "Чтобы сообщить о сборе мусора, нажмите кнопку:",
        reply_markup=get_report_kb(user_id)
    )
    # Важно: сбрасываем любые «зависшие» состояния, чтобы не было конфликтов
    await state.clear()
    return  # Прерываем: дальше другие хендлеры НЕ должны срабатывать


# --- Запуск ---
async def main():
    await init_db()

    # Настройка и запуск планировщика
    scheduler.add_job(
        send_weekly_poll,
        CronTrigger(hour=16, minute=00, day_of_week='mon'),
        id='weekly_poll_job',
        replace_existing= True # <-- если задача уже есть, заменит её, а не добавит новую
    )  # каждый день в 10:00

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
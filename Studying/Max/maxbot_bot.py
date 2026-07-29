import asyncio
import logging
from datetime import datetime
import aiosqlite

from maxbot.bot import Bot
from maxbot.dispatcher import Dispatcher
from maxbot.filters import F, StateFilter, TextStartsFilter
from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


bot = Bot('f9LHodD0cOLIMSeObumpLGeRdVcXKpqBdIUzZka9VEMjb0Ly20JFepfmJXrBsuUprbbn99WR5zLm7pfQfMcH')
DB_PATH = "trash_report.db"
dp = Dispatcher(bot)

# --- Константы и утилиты ---
RUSSIAN_LETTERS = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

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

class Registration(StatesGroup):
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
                house_number INTEGER NOT NULL,
                answer TEXT,
                report_date TEXT NOT NULL,
                UNIQUE(user_id, report_date)
            )
        """)
        await db.commit()

async def register_user(user_id: int, name: str, street: str, house_number: int):
    today = get_today_str()
    async with aiosqlite.connect(DB_PATH) as db:
        try:
            await db.execute(
                """
                INSERT INTO trash_reports (user_id, user_name, street, house_number, answer, report_date)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, name, street, house_number, None, today)
            )
            await db.commit()
        except aiosqlite.IntegrityError:
            pass

async def save_or_update_report(user_id: int, answer: str):
    today = get_today_str()
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "UPDATE trash_reports SET answer = ? WHERE user_id = ? AND report_date = ?",
                (answer, user_id, today)
            )
            if cursor.rowcount > 0:
                await db.commit()
                return "updated", today

            cur = await db.execute(
                "SELECT user_name, street, house_number FROM trash_reports WHERE user_id = ? LIMIT 1",
                (user_id,)
            )
            row = await cur.fetchone()

            if not row:
                raise ValueError("Пользователь не зарегистрирован")

            name, street, house_number = row

            await db.execute(
                """
                INSERT INTO trash_reports (user_id, user_name, street, house_number, answer, report_date)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, name, street, house_number, answer, today)
            )
            await db.commit()
            return "inserted", today
    except Exception as e:
        print(f"Ошибка при сохранении отчёта: {e}")
        return None, None

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

def get_2_buttons_keyboard():
    builder = InlineKeyboardBuilder()
    btn1 = CallbackButton(text="Кнопка 1", payload="btn_1")
    btn2 = CallbackButton(text="Кнопка 2", payload="btn_2")
    builder.row(btn1, btn2)
    return builder.as_markup()

def get_streets_kb(page=0, per_page=6):
    start = page * per_page
    end = start + per_page
    page_streets = streets_list[start:end]

    builder = InlineKeyboardBuilder()
    row_buttons = []

    # Группируем по 3 кнопки в строку
    for idx, street in enumerate(page_streets):
        global_idx = start + idx
        btn = CallbackButton(
            text=street,
            payload=f"s_{global_idx}"
        )
        row_buttons.append(btn)

        # Если набрали 3 кнопки — делаем строку
        if len(row_buttons) == 2:
            builder.row(*row_buttons)
            row_buttons = []

    # Если остались кнопки (меньше 3) — добавляем последнюю строку
    if row_buttons:
        builder.row(*row_buttons)

    # Навигация
    nav_buttons = []
    if page >0:
        nav_buttons.append(
            CallbackButton(
                text="← Назад",
                payload=f"streets_page_{page - 1}"
            )
        )
    if end < len(streets_list):
        nav_buttons.append(
            CallbackButton(
                text="Вперёд →",
                payload=f"streets_page_{page + 1}"
            )
        )

    if nav_buttons:
        builder.row(*nav_buttons)

    return builder.as_markup()


def get_report_kb():
    builder = InlineKeyboardBuilder()
    btn_report = CallbackButton(text='Сообщить о сборе мусора',payload='Report a trash collection')
    builder.row(btn_report)
    return builder.as_markup()

def get_yes_no_kb():
    builder = InlineKeyboardBuilder()

    btn_yes = CallbackButton(text='Да',payload='yes')
    btn_no = CallbackButton(text='Нет',payload='no')

    builder.row(btn_yes,btn_no)

    return builder.as_markup()

# --- Хендлеры ---

@dp.message(Command('start'))
async def start_handler(event: MessageCreated):
    await event.message.answer(
        text='Привет! 👋\nЯ простой бот на MaxAPI.',
        attachments=[get_2_buttons_keyboard()]
    )

@dp.callback(F)
async def press_btn_1(event: MessageCallback):
    await event.message.answer(text="Вы нажали кнопку 1", attachments=[get_2_buttons_keyboard()])

@dp.callback()
async def press_btn_2(cb):
    if cb == 'btn_2':
        await bot.send_message(cb.user.id,text="Вы нажали кнопку 2", attachments=[get_2_buttons_keyboard()])

@dp.callback(F.callback.payload == 'yes')
async def press_btn_yes(event: MessageCallback):
    await event.message.answer(text=f"Ваша улица: {event.message.body.text}")

@dp.callback(F.callback.payload == 'no')
async def press_btn_no(event: MessageCallback, state):
    kb = get_streets_kb(page=0, per_page=6)
    await state.set_state(Registration.fill_street)
    await event.message.answer("Выберите улицу:", attachments=[kb])

@dp.callback()
async def handle_streets(event: MessageCallback):
    payload = event.callback.payload
    logging.info("Получен payload: %s", payload)

    # Выбор улицы
    if payload.startswith("s_"):
        try:
            idx_str = payload.split("_")[1]
            idx = int(idx_str)

            # ПРОВЕРКА ГРАНИЦ — самое важное
            if idx < 0 or idx >= len(streets_list):
                logging.error(f"Индекс {idx} вне диапазона [0, {len(streets_list)-1}]")
                await event.message.answer("❌ Произошла ошибка при выборе улицы. Пожалуйста, нажмите кнопку ещё раз или начните заново.")
                return

            chosen_street = streets_list[idx]
            await event.message.answer(
                f"{chosen_street}",
                attachments=[get_yes_no_kb()]
            )
        except (IndexError, ValueError) as e:
            logging.error(f"Некорректный payload: {payload}, ошибка: {e}")
            await event.message.answer("❌ Произошла ошибка при выборе улицы. Попробуйте снова.")

    # Пагинация
    elif payload.startswith("streets_page_"):
        try:
            page = int(payload.split("_")[-1])
            kb = get_streets_kb( page=page, per_page=6)


            await event.edit(
                text="Выберите улицу:",
                attachments=[kb]
            )
        except Exception as e:
            logging.error(f"Ошибка при пагинации: {e}")
            await event.message.answer("❌ Не удалось обновить список улиц. Попробуйте ещё раз.")

@dp.message()
async def unregistered_guard(event: MessageCreated, state:FSMContext):
    msg = event.message
    user_id = event.from_user.user_id
    current_state = await state.se

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
            attachments=[get_streets_kb()]
        )
        await state.set_state(Registration.fill_street)
        return  # Важно: дальше не идём

    # Пользователь зарегистрирован: показываем главное меню и прерываем
    logger.info(f"[GUARD] Пользователь {user_id} найден → показываем меню")
    await msg.answer(
        "Чтобы сообщить о сборе мусора, нажмите кнопку:",
        attachments=[get_report_kb()]
    )
    # Важно: сбрасываем любые «зависшие» состояния, чтобы не было конфликтов
    await state.clear()
    return  # Прерываем: дальше другие хендлеры НЕ должны срабатывать

@dp.message()
async def echo_handler(event: MessageCreated):
    if event.message.body.text:
        await event.message.answer(f"Вы написали: {event.message.body.text}")
        kb = get_streets_kb(page=0, per_page=6)
        await event.message.answer("Выберите улицу:", attachments=[kb])

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

import os
import asyncio
import logging
from datetime import datetime, timedelta
import aiosqlite
import re


from maxapi.filters.middleware import HandlerCallable, BaseMiddleware
from maxapi.types import  UpdateUnion, Message, BotStarted
from maxapi import Bot, Dispatcher, Router, F
from maxapi.context import StatesGroup, State, MemoryContext
from maxapi.filters import StateFilter
from maxapi.types import MessageCreated, Command, CallbackButton, MessageCallback
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from typing_extensions import Any


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GlobalMessageLoggerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: HandlerCallable,
            event: UpdateUnion,
            data: dict[str, Any],
    ) -> Any:

        # Args:
        # handler: Хендлер события.
        # event_object: Событие.
        # data: Дополнительные данные.
        # Получаем текущее состояние из контекста (data)
        # В aiogram 3 состояние хранится в data['state']

        # if user_username:
        #     link = f"https://max.ru/@{user_username}"
        # else:
        #     link = None  # ссылки нет

        if isinstance(event, MessageCreated):
            # Формируем лог
            text = event.message.body.text
        elif isinstance(event, MessageCallback):
            text = event.callback.payload
        else:
            logger.warning("Не удалось получить пользователя из события")
            return await handler(event, data)

        log_msg = f'Сообщение от {event.from_user.first_name}\nid:{event.from_user.user_id}\nТекст: {text}'
        logger.info(f"[GUARD] {log_msg}")

        if ADMINS_IDS:
            try:
                #Если это сообщение не от самого себя
                if event.from_user.user_id not in ADMINS_IDS:
                    await bot.send_message(
                        user_id=ADMINS_IDS[0],
                        text=log_msg
                    )
            except Exception as e:
                logger.error(f"Не удалось отправить уведомление админу: {e}")

        # Передаем управление дальше (следующему middleware или хендлеру)

        return await handler(event, data)


BOT_TOKEN = os.getenv('BOT_TOKEN_max_1')
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в окружении")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()  # В maxapi 1.2.1 storage не нужен
router = Router()

DB_PATH = "trash_report.db"

# --- ВАЖНО: Подключаем middleware здесь ---
dp.register_outer_middleware(GlobalMessageLoggerMiddleware())

# -------------------------------------------
scheduler = AsyncIOScheduler()

# --- Константы и утилиты ---
RUSSIAN_LETTERS = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

ADMINS_IDS = [230811110]
SUB_ADMINS_IDS = [16496774] #Светлана
CONTACTS = ['+7 918 414 78 32']


HOUSE_PATTERN = re.compile(
    r'^\d{1,4}$|'                        # Просто число (1, 20, 108)
    r'^\d{1,4}[а-яА-ЯёЁ]$|'              # Число + одна буква (1в, 20а)
    r'^\d{1,4}/\d{1,4}$|'                # Дробь из двух чисел (1/2, 12/3)
    r'^\d{1,4}[а-яА-ЯёЁ]/\d{1,4}$|'      # Число+буква / число (1в/22, 10а/5)
    r'^\d{1,4}/\d{1,4}[а-яА-ЯёЁ]$|'      # Число / число+буква (1/2в, 12/3а)
    r'^\d{1,4}[а-яА-ЯёЁ]/\d{1,4}[а-яА-ЯёЁ]$'  # Число+буква / число+буква (3б/12г)
)




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

kostroma_streets = ["Ул. Индустриальная", "д. Самково", "Ул. Свердлова", 'Ул. Южная', 'Ул. Магистральная',
                    'Ул. Костромская']
kirgach_streets = ['кв-л Южный', 'Ул. Самостроевская', 'Ул. Ново-Полянская']

# Добавление улиц из других городов
streets_list += kostroma_streets
streets_list += kirgach_streets
streets_list.sort()


class Registration(StatesGroup):
    fill_street = State()
    street_confirming = State()
    fill_house_number = State()
    confirm_house_number = State()

def get_today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def get_iso_week(date_str: str) -> tuple[int, int]:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.isocalendar()[:2]
    except Exception:
        return (0, 0)


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
            print("Пользователь не зарегистрирован")

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

async def get_statistic(message:Message ,filter_type:str):

    # Получение текущей даты для формирования сообщения
    today = get_today_str()
    iso_year, iso_week = get_iso_week(today)
    date = get_week_range_text(today)

    #Создание сообщения
    text = ""
    text += date + ':\n\n'


    async with aiosqlite.connect(DB_PATH) as db:
        # Базовый запрос без фильтрации по статусу
        query = """
            SELECT user_id, user_name, street, house_number, answer, report_date
            FROM trash_reports
            WHERE iso_year = ? AND iso_week = ?
        """
        params = [iso_year, iso_week]


        if filter_type == "Без ответа":
            # Берём строки, где answer НЕ заполнен (NULL или пустая строка)
            query += " AND (answer IS NULL OR answer = '')"
        elif filter_type in ("Да", "Нет"):
            # Только конкретные статусы
            query += " AND answer = ?"
            params.append(filter_type)
        else:
            # На всякий случай: если вдруг придёт что-то неожиданное — не фильтруем по answer
            pass

        cursor = await db.execute(query, params)
        rows = await cursor.fetchall()

        if not rows:
            await message.answer(f"За неделю {date} таких отчётов нет.")
            #Небольшая пауза
            await asyncio.sleep(0.5)
            # Показываем кнопки
            await message.answer(
                f"Выберите тип статистики за неделю\n{date}:",
                attachments=[get_statistic_kb()]
            )
            return




        for row in rows:
            user_id, user_name, street, house_number, answer, report_date = row

            if answer == "Да":
                symb = "✅"
            elif answer == "Нет":
                symb = "❌"
            else:
                symb = "➖️"



            text += (
                f"Пользователь: {user_name}\n"
                f"Адрес: {street} {house_number}\n"
                f"Ответ: {symb}{answer}\n\n"
            )
        # f"Дата: {report_date}\n"

        await message.answer(text=text)
        # Небольшая пауза
        await asyncio.sleep(0.5)
        # Показываем кнопки
        await message.answer(
            f"Выберите тип статистики за неделю\n{date}:",
            attachments=[get_statistic_kb()]
        )


# Остальные функции БД (save_or_update_report, get_last_report и т.д.) можно оставить как есть

# --- Клавиатуры ---


def get_streets_kb():
    builder = InlineKeyboardBuilder()
    row_buttons = []

    for street_name in streets_list:
        btn = CallbackButton(
            text=street_name,
            payload=f"{street_name}"
        )
        row_buttons.append(btn)

        if len(row_buttons) == 2:  # оставил как у тебя, но логичнее 3
            builder.row(*row_buttons)
            row_buttons = []

    if row_buttons:
        builder.row(*row_buttons)

    builder.row()

    return builder.as_markup()


def get_report_kb():
    builder = InlineKeyboardBuilder()
    btn_report = CallbackButton(text='Сообщить о сборе мусора', payload='Сообщить о сборе мусора')
    builder.row(btn_report)
    return builder.as_markup()


def get_yes_no_kb():
    builder = InlineKeyboardBuilder()
    btn_yes = CallbackButton(text='Да', payload='да')
    btn_no = CallbackButton(text='Нет', payload='нет')
    builder.row(btn_yes, btn_no)
    return builder.as_markup()


def get_yes_no_trash_kb():
    builder = InlineKeyboardBuilder()
    btn_yes = CallbackButton(text="Да, собран", payload='Да, собран')
    btn_no = CallbackButton(text="Нет, не собран", payload='Нет, не собран')
    builder.row(btn_yes, btn_no)
    return builder.as_markup()


def get_edit_kb():
    builder = InlineKeyboardBuilder()
    btn = CallbackButton(text="Изменить ответ", payload="Изменить ответ")
    builder.row(btn)
    return builder.as_markup()


def get_restart_kb():
    builder = InlineKeyboardBuilder()
    btn = CallbackButton(text="Начать сначала", payload="Начать сначала")
    builder.row(btn)
    return builder.as_markup()

def get_statistic_kb():
    builder = InlineKeyboardBuilder()
    btn_all = CallbackButton(text="Полная", payload="Полная")
    btn_yes = CallbackButton(text="Да", payload="Да")
    btn_no = CallbackButton(text="Нет", payload="Нет")
    btn_none = CallbackButton(text="Без ответа", payload="Без ответа")
    builder.row(btn_all)
    builder.row(btn_yes)
    builder.row(btn_no)
    builder.row(btn_none)
    return builder.as_markup()

def get_commands_kb():
    builder = InlineKeyboardBuilder()
    btn_repeat = CallbackButton(text='Повторить рассылку',payload='Повторить рассылку')
    builder.row(btn_repeat)
    return builder.as_markup()


# --- Рассылка ---
async def send_daily_reminder_to_admins():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT DISTINCT user_id FROM trash_reports WHERE answer IS NULL OR answer ='' ") as cursor:
            rows = await cursor.fetchall()

    if not rows:
        return

    for (user_id,) in rows:
        if user_id not in ADMINS_IDS:
            continue  # пропускаем не-админов

        try:
            await bot.send_message(
                user_id=user_id,
                text="Напоминаем: пожалуйста, сообщите, забрали ли мусор у вашего дома?",
                attachments=[get_yes_no_trash_kb()]
            )
        except Exception as e:
            print(f"Не удалось отправить админу {user_id}: {e}")


async def send_weekly_reminder_to_users(event=None):

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT DISTINCT user_id,user_name,street,house_number FROM trash_reports WHERE answer IS NULL OR answer ='' ") as cursor:
            rows = await cursor.fetchall()

    if not rows:
        await bot.send_message(
            user_id=event.from_user.user_id,
            text="Нет пользователей, не ответивших на этой неделе"
        )
        return

    for (user_id,user_name,street,house_number) in rows:
        # if user_id in ADMINS_IDS:
        #     continue  # пропускаем админов — им уже шлём ежедневно

        try:
            await bot.send_message(
                user_id=user_id,
                text="Напоминаем: пожалуйста, сообщите, забрали ли мусор у вашего дома?",
                attachments=[get_yes_no_trash_kb()]
            )

            #Оповещение администратору в случае частного запроса
            if event:
                await bot.send_message(user_id=event.from_user.user_id,
                text=f'Напомнили пользователю:\n'
                     f'Имя: {user_name}\n'
                     f'Адрес: {street} {house_number}'
                                       )


        except Exception as e:
            print(f"Не удалось отправить пользователю {user_id}: {e}")

# --- Хендлеры ---



@router.bot_started()
async def start_handler(event:BotStarted):

    await bot.send_message(event.chat_id,
        text='Привет! 👋\nЯ простой бот.\nНапиши мне любое сообщение'
    )

@router.message_created(Command('stat'))
async def cmd_stat(event: MessageCreated):
    message = event.message

    #Получение текущей даты для формирования сообщения
    today = get_today_str()
    date = get_week_range_text(today)

    # Проверка прав админа
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS:
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    # Показываем кнопки
    await message.answer(
        f"Выберите тип статистики за неделю\n{date}:",
        attachments=[get_statistic_kb()]
    )

@router.message_created(Command('commands'))
async def cmd_commands(event: MessageCreated):
    message = event.message

    # Проверка прав админа
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS:
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    await message.answer('Выберите доступные команды',attachments=[get_commands_kb()])

@router.message_callback(F.callback.payload.in_(streets_list), Registration.fill_street)
async def fill_street_process(event: MessageCallback, context: MemoryContext):
    message = event.message
    street = event.callback.payload

    await context.update_data(street=street)
    await message.answer(
        f"Ваша улица: {street}.\nВерно?",
        attachments=[get_yes_no_kb()]
    )
    await context.set_state(Registration.street_confirming)


@router.message_callback(F.callback.payload.in_(['да', 'нет']), Registration.street_confirming)
async def handle_street_confirm(event: MessageCallback, context: MemoryContext):
    message = event.message
    data = await context.get_data()
    street = data.get('street')

    if not street:
        # Если улицы нет — значит, пользователь нажал кнопку без выбора, возвращаем к выбору
        kb = get_streets_kb()
        await message.answer("Сначала выберите улицу:", attachments=[kb])
        return

    if event.callback.payload == 'да':
        await message.answer(f"Ваша улица: {street}\nНапишите номер дома:")
        await context.set_state(Registration.fill_house_number)
    else:
        kb = get_streets_kb()
        await context.set_state(Registration.fill_street)
        await context.update_data(street=None)
        await message.answer("Выберите улицу:", attachments=[kb])


@router.message_created(Registration.fill_house_number)
async def fill_house_number(event: MessageCreated, context: MemoryContext):
    message = event.message
    text = message.body.text.strip().upper()

    if not HOUSE_PATTERN.match(text):
        await message.answer("Введите корректный номер дома.\n"
                             "Примеры: 14, 20В, 10/2, 1В/22",
                             attachments=[get_restart_kb()])
        return

    await context.update_data(house_number=text)
    await context.set_state(Registration.confirm_house_number)  # переходим к подтверждению
    await message.answer(f"Номер дома: {text}\nПодтвердите, пожалуйста:", attachments=[get_yes_no_kb()])


@router.message_callback(F.callback.payload.in_(['да', 'нет']), Registration.confirm_house_number)
async def confirm_house_number(event: MessageCallback, context: MemoryContext):
    message = event.message
    data = await context.get_data()
    house_number = data.get('house_number')

    if not house_number:
        # Защита от странного поведения
        await message.answer("Что-то пошло не так. Начните заново.")
        await context.clear()
        return

    if event.callback.payload == 'да':
        # Здесь можно сразу делать проверку на дубликат в БД и сохранять
        user_id = event.from_user.user_id
        name = data.get('name', 'Неизвестно')
        street = data.get('street', 'Неизвестно')

        # Вызови свою функцию регистрации/проверки, например:
        if await register_user(user_id, name, street, house_number):

            await message.answer(
                text=f"Благодарю! Ваша анкета:\n\n"
                     f"Имя: {name}\n"
                     f"Адрес: {street} {house_number}"
            )

            await message.answer(
                "Адрес успешно сохранён! Теперь вы можете сообщать о сборе мусоре.",
                attachments=[get_report_kb()])
            await context.clear()
            # показать главное меню
        else:
            await message.answer("Такой адрес уже есть в базе. Начните заново и выберите другой адрес.")
            # можно вернуть к выбору улицы
            await context.set_state(Registration.fill_street)
            kb = get_streets_kb()
            await message.answer("Выберите другую улицу:", attachments=[kb])
    else:
        await context.set_state(Registration.fill_house_number)
        await message.answer("Пожалуйста, введите номер дома заново:")


@router.message_created(Registration.fill_house_number)
async def fill_house_letter(event: MessageCreated, context: MemoryContext):
    message = event.message
    text = message.body.text.strip()

    if not text.isdigit() or int(text) not in range(1, 501):
        await message.answer("Введите корректный номер дома:", attachments=[get_restart_kb()])
        return

    await context.update_data(house_number=text)
    await context.set_state(Registration.confirm_house_number)  # переходим к подтверждению
    await message.answer(f"Номер дома: {text}\nПодтвердите, пожалуйста:", attachments=[get_yes_no_kb()])



@router.message_callback(F.callback.payload == 'Начать сначала',Registration)
async def restart_registration(event: MessageCreated, context: MemoryContext):
    message = event.message
    await event.message.delete() #Удалить сообщение
    await context.clear()
    await context.set_state(Registration.fill_street)

    await context.update_data(name=event.from_user.full_name)
    await message.answer("Выберите улицу:", attachments=[get_streets_kb()])


@router.message_callback(F.callback.payload == 'Сообщить о сборе мусора')
async def ask_status(event: MessageCallback):
    message = event.message
    await message.answer("Мусор собран?", attachments=[get_yes_no_trash_kb()])


@router.message_callback(F.callback.payload.in_(["Да, собран", "Нет, не собран"]))
async def handle_yes_no(event: MessageCallback):
    message = event.message
    user_id = event.from_user.user_id
    answer_map = {"Да, собран": "Да", "Нет, не собран": "Нет"}
    new_answer = answer_map[event.callback.payload]

    result, _ = await save_or_update_report(user_id, new_answer)

    # Получаем актуальную запись, чтобы взять её report_date
    record = await get_last_report(user_id)
    if not record:
        await message.answer("Не удалось найти запись.")
        return

    week_range = get_week_range_text(record["report_date"])

    if new_answer == 'Да':
        symb = '✅️'
    else:
        symb = '❌️'



    if result == "updated":
        await message.answer(
            f"Статус за неделю\n{week_range} обновлён: \n\n«{symb}{new_answer}».",
            attachments=[get_edit_kb()]
        )
    else:
        await message.answer(f"Записана новая отметка за неделю\n{week_range}:\n\n«{symb}{new_answer}».",
                             attachments=[get_edit_kb()])


@router.message_callback(F.callback.payload == "Изменить ответ")
async def cb_edit(event: MessageCallback):
    message = event.message
    user_id = event.from_user.user_id
    record = await get_last_report(user_id)

    if not record:
        await message.answer("Нет записей для редактирования.")
        return

    if not await can_edit_record(record["report_date"]):
        week_range = get_week_range_text(record["report_date"])
        await message.answer(
            f"❌ Нельзя изменить запись за неделю\n{week_range}:\nона старше текущей календарной недели."
        )
        return

    week_range = get_week_range_text(record["report_date"])
    new_answer = record['answer']
    if new_answer == 'Да':
        symb = '✅️'
    else :
        symb = '❌️'


    await message.answer(
        f"Текущая запись за неделю\n{week_range}:\n\n«{symb}{record['answer']}».\n\nВыберите новый статус:",
        attachments=[get_yes_no_trash_kb()]
    )


# ГЛАВНЫЙ ХЕНДЛЕР-СТРАЖ — только для сообщений, когда пользователь НЕ в FSM
@router.message_created(StateFilter(None))
async def unregistered_guard(event: MessageCreated, context: MemoryContext):
    message = event.message
    user = event.from_user
    user_id = event.from_user.user_id

    # Проверяем, есть ли пользователь в БД
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT 1 FROM trash_reports WHERE user_id = ?",
            (user_id,)
        )
        exists = await cursor.fetchone()

    if not exists:
        logger.info(f"[GUARD] Пользователь {user_id} НЕ найден → регистрация")
        await context.update_data(name=user.full_name)
        kb = get_streets_kb()
        await message.answer(
            f"Привет, {user.first_name}!\nПредлагаю познакомиться!\nВыберите улицу:",
            attachments=[kb]
        )
        await context.set_state(Registration.fill_street)
        return

    # Пользователь зарегистрирован
    logger.info(f"[GUARD] Пользователь {user_id} найден → показываем меню")
    await message.answer(
        f"Вы написали: '{message.body.text}'.\nЧтобы сообщить о сборе мусора, нажмите кнопку:",
        attachments=[get_report_kb()]
    )
    # Сбрасываем состояние, если оно осталось «зависшим»
    await context.clear()
    return


@router.message_callback(F.callback.payload.in_(["Полная", "Да", "Нет","Без ответа"]))
async def handle_stat_buttons(event:MessageCallback):
    message = event.message
    # Проверка прав админа (обязательно и тут!)
    if event.callback.user.user_id not in ADMINS_IDS and event.callback.user.user_id not in SUB_ADMINS_IDS :
        await message.answer("❌ Доступ запрещён")
        return

    # Вызываем статистику. Передаём event., потому что get_statistic ждёт MessageCreated
    await get_statistic(message=message, filter_type=event.callback.payload)

@router.message_callback(F.callback.payload == 'Повторить рассылку')
async def handle_command_repeat_mailing(event:MessageCallback):
    message = event.message
    # Проверка прав админа (обязательно и тут!)
    if event.callback.user.user_id not in ADMINS_IDS and event.callback.user.user_id not in SUB_ADMINS_IDS :
        await message.answer("❌ Доступ запрещён")
        return

    await send_weekly_reminder_to_users(event)


# Эхо-хендлер — только если пользователь в каком-то состоянии (например, в форме)
# Если ты хочешь вообще отключить эхо — просто удали этот хендлер
@router.message_created()
async def echo_handler(event: MessageCreated, context: MemoryContext):
    message = event.message
    current_state = await context.get_state()
    if current_state is None:
        # Если пользователь не в FSM, этот хендлер не должен срабатывать,
        # потому что выше уже есть guard с StateFilter(None).
        # Но если вдруг сработает — просто игнорируем.
        return

    text = message.body.text
    if text:
        await message.answer(f"Вы написали: '{text}'.\nПродолжайте заполнять форму.", attachments=[get_restart_kb()])


async def main():
    await init_db()
    dp.include_routers(router)
    # Настройка и запуск планировщика
    scheduler.add_job(
        send_daily_reminder_to_admins,
        CronTrigger(hour=9, minute=0),  # Каждый день
        id='weekly_poll_admins',
        replace_existing=True  # <-- если задача уже есть, заменит её, а не добавит новую
    )  # каждый день в 9:00

    scheduler.add_job(
        send_weekly_reminder_to_users,
        CronTrigger(hour=16, minute=0,day_of_week='mon'),  # day_of_week='mon'
        id='weekly_poll_users',
        replace_existing=True  # <-- если задача уже есть, заменит её, а не добавит новую
    )  # каждый день в 16:00

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

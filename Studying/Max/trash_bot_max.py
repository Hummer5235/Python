import os
import asyncio
import logging
from datetime import datetime, timedelta
import aiosqlite
import re


from maxapi.filters.middleware import HandlerCallable, BaseMiddleware
from maxapi.types import UpdateUnion, Message, BotStarted, BotCommand
from maxapi import Bot, Dispatcher, Router, F
from maxapi.context import StatesGroup, State, MemoryContext
from maxapi.filters import StateFilter
from maxapi.types import MessageCreated, Command,  MessageCallback
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from typing_extensions import Any

from Count_month_payments import count_payments
from Project.keyboards.keyboards import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GlobalMessageLoggerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: HandlerCallable,
            event: UpdateUnion,
            data: dict[str, Any],
    ) -> Any:



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

class Commands(StatesGroup):
    count_payments = State()
    get_statistic = State()
    create_a_newsletter = State()
    create_a_newsletter_confirm = State()
    confirm_repeat_mailing = State()




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
        await db.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_week ON trash_reports(user_id, iso_year, iso_week)")

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

    symb_dict = {
        'Полная':"✅❌➖️",
        'Да':"✅",
        'Нет':"❌",
        'Без ответа':"➖️"
    }

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

        if filter_type == 'Без ответа' or filter_type == 'Полная':
            kb = get_commands_kb()
        else:
            kb = get_statistic_kb()

        if not rows:
            await message.edit(
                f"Выборка: {symb_dict[filter_type]}{filter_type}\n\n"
                f"За неделю {date} таких отчётов нет.",
                attachments=[kb]
            )
            return

        text = (f'Выборка: {symb_dict[filter_type]}{filter_type}\n\n'
                f'{date}:\n\n')



        #Перебираем ответы пользователей
        for row in rows:
            user_id, user_name, street, house_number, answer, report_date = row

            #Каждому ответу свой символ
            if answer in ('Да','Нет'):
                user_symb = symb_dict[answer]
            else:
                user_symb = '➖️'
            text += (
                f"Пользователь: {user_name}\n"
                f"Адрес: {street} {house_number}\n"
                f"Ответ: {user_symb}{answer}\n\n"
            )

        await message.edit(text,attachments=[kb])


# Остальные функции БД (save_or_update_report, get_last_report и т.д.) можно оставить как есть




# --- Рассылка ---
async def send_daily_reminder_to_admins():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT DISTINCT user_id "
                              "FROM trash_reports "
                              "WHERE answer IS NULL OR answer ='' ") as cursor:
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


    #Получаем текущую неделю
    today = get_today_str()
    iso_year, iso_week = get_iso_week(today)

    #Проверяем всех, кто не ответил на этой неделе
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
        SELECT DISTINCT user_id,user_name,street,house_number 
        FROM trash_reports 
        WHERE (answer IS NULL OR answer ='') AND iso_year= ? AND iso_week = ?""",[iso_year, iso_week]) as cursor:

            rows = await cursor.fetchall()
            if not rows:
                # Если это ручная рассылка при помощи команды
                if event:
                    await event.message.edit("Нет пользователей, не ответивших на этой неделе",
                        attachments=[get_statistic_kb()]
                    )
                    return

            # Определяем, кому слать отчёт о рассылке
            report_receiver_id = event.from_user.user_id if event else ADMINS_IDS[0]

            for (user_id, user_name, street, house_number) in rows:
                # if user_id in ADMINS_IDS:
                #     continue  # пропускаем админов — им уже шлём ежедневно

                try:
                    await bot.send_message(
                        user_id=user_id,
                        text="Напоминаем: пожалуйста, сообщите, забрали ли мусор у вашего дома?",
                        attachments=[get_yes_no_trash_kb()]
                    )

                    # Оповещение администратору в случае частного запроса
                    await bot.send_message(user_id=report_receiver_id,
                                           text=f'Напомнили пользователю:\n'
                                                f'Имя: {user_name}\n'
                                                f'Адрес: {street} {house_number}'
                                           )



                except Exception as e:
                    print(f"Не удалось отправить пользователю {user_id}: {e}")



#Рассылка новостного сообщения пользователям
async def mailing_newsletter(event, message_for_news_letter):

    message = event.message

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
        SELECT DISTINCT user_id,user_name,street,house_number
        FROM trash_reports """) as cursor:

            rows = await cursor.fetchall()
            if not rows:
                await message.answer(
                    text='Нет пользователей для рассылки'
                )
            else:



                for row in rows:
                    user_id, user_name,street, house_number = row

                    try:

                        await bot.send_message(
                            user_id=user_id,
                            text= message_for_news_letter
                        )

                        await message.answer(
                                               text=f'✅Оповестили пользователя:\n\n'
                                                    f'Имя: {user_name}\n'
                                                    f'Адрес: {street} {house_number}'
                                               )
                    except:
                        await message.answer(
                            text=f'❌Отправка пользователю:\n\n'
                                 f'Имя: {user_name}\n'
                                 f'Адрес: {street} {house_number}\n'
                                 f'id: {user_id}\n\n'
                                 f'Не удалась'
                        )

#Программы выполняется утром в понедельник
async def users_to_new_week():

    today = datetime.now()
    iso_year_curr, iso_week_curr, _ = today.isocalendar()


    today = datetime.now()
    # Корректно считаем прошлую ISO-неделю
    if iso_week_curr == 1:
        ref = today - timedelta(days=7)
        iso_year_prev, iso_week_prev, _ = ref.isocalendar()
    else:
        iso_year_prev = iso_year_curr
        iso_week_prev = iso_week_curr - 1

    report_date_str = get_today_str()

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO trash_reports (
                user_id, user_name, street, house_number,
                iso_year, iso_week, report_date, answer
            )
            SELECT user_id, user_name, street, house_number, ?, ?, ?, NULL
            FROM trash_reports
            WHERE iso_year = ? AND iso_week = ?
            """,
            (iso_year_curr, iso_week_curr, report_date_str, iso_year_prev, iso_week_prev)
        )
        await db.commit()

# --- Хендлеры ---






@router.bot_started()
async def start_handler(event:BotStarted):

    await bot.send_message(event.chat_id,
        text='Привет! 👋\nЯ простой бот.\nНапиши мне любое сообщение'
    )


async def send_stat_menu(event):

    # Получение текущей даты для формирования сообщения
    today = get_today_str()
    date = get_week_range_text(today)

    message = event.message

    # Проверка прав админа
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS:
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    if isinstance(event,MessageCreated): #Если это сообщение и нужно именно ответить
        await message.answer(
            f"Выберите тип статистики за неделю\n{date}:",
            attachments=[get_statistic_types_kb()]
        )
        return

    # Показываем кнопки
    await message.edit(
        f"Выберите тип статистики за неделю\n{date}:",
        attachments=[get_statistic_types_kb()]
    )

@router.message_created(Command('stat'))
async def cmd_stat(event,context : MemoryContext):
        await context.set_state(Commands.get_statistic)
        await send_stat_menu(event)

@router.message_callback(F.callback.payload=='Получить статистику')
async def cb_stat(event,context : MemoryContext):
        await context.set_state(Commands.get_statistic)
        await send_stat_menu(event)

@router.message_created(Command('payments'))
async def cmd_payments(event,context :MemoryContext):
    message = event.message

    #Проверка
    #прав
    #админа

    if event.from_user.user_id not in ADMINS_IDS :
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    await message.answer(
        text='Отправьте список оплат в формате:\n'
             '(Стоимость) день,день...\n'
             '(Стоимость) день,день...\n\n'
             'Пример:\n'
             '(1000) 1,8,15,22,29\n'
             '(1200) 1,8,15,22,29'
    )

    await context.set_state(Commands.count_payments)


@router.message_created(Command('newsletter'))
async def cmd_newsletter(event:MessageCreated,context : MemoryContext):
    message = event.message

    # Проверка прав админа
    if event.from_user.user_id not in ADMINS_IDS:
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    await message.answer(
        'Напишите сообщение для пользователей:'
    )

    await context.set_state(Commands.create_a_newsletter)

@router.message_created(Command('commands'))
async def cmd_commands(event: MessageCreated):
    message = event.message

    # Проверка прав админа и суб_админа
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS:
        await message.answer("❌ Доступ запрещён: вы не администратор.")
        return

    await message.answer('Выберите доступные команды:',attachments=[get_commands_kb()])





@router.message_callback(F.callback.payload.in_(streets_list), Registration.fill_street)
async def fill_street_process(event: MessageCallback, context: MemoryContext):
    message = event.message
    street = event.callback.payload

    await context.update_data(street=street)
    await message.edit(
        f"Ваша улица: {street}.\nВерно?",
        attachments=[get_yes_no_kb()]
    )
    await context.set_state(Registration.street_confirming)


@router.message_callback(F.callback.payload.in_(['Да', 'Нет']), Registration.street_confirming)
async def handle_street_confirm(event: MessageCallback, context: MemoryContext):
    message = event.message
    data = await context.get_data()
    street = data.get('street')

    if not street:
        # Если улицы нет — значит, пользователь нажал кнопку без выбора, возвращаем к выбору
        kb = get_streets_kb(streets_list)
        await message.answer("Сначала выберите улицу:", attachments=[kb])
        return

    if event.callback.payload == 'Да':
        await message.edit(f"Ваша улица: {street}\nНапишите номер дома:",attachments=[])
        await context.set_state(Registration.fill_house_number)
    else:
        kb = get_streets_kb(streets_list)
        await context.set_state(Registration.fill_street)
        await context.update_data(street=None)
        await message.edit("Выберите улицу:", attachments=[kb])


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


@router.message_callback(F.callback.payload.in_(['Да','Нет']), Registration.confirm_house_number)
async def confirm_house_number(event: MessageCallback, context: MemoryContext):
    message = event.message
    data = await context.get_data()
    house_number = data.get('house_number')

    if not house_number:
        # Защита от странного поведения
        await message.answer("Что-то пошло не так. Начните заново.")
        await context.clear()
        return

    if event.callback.payload == 'Да':
        # Здесь можно сразу делать проверку на дубликат в БД и сохранять
        user_id = event.from_user.user_id
        name = data.get('name', 'Неизвестно')
        street = data.get('street', 'Неизвестно')

        # Вызови свою функцию регистрации/проверки, например:
        if await register_user(user_id, name, street, house_number):

            await message.edit(
                text=f"Благодарю! Ваша анкета:\n\n"
                     f"Имя: {name}\n"
                     f"Адрес: {street} {house_number}\n\n"
                     f"Бот будет опрашивать вас раз в неделю.\nТакже вы сможете сообщать о сборе мусоре самостоятельно на кнопку.",
                attachments=[get_report_kb()]
            )

            await context.clear()
            # показать главное меню
        else:
            # можно вернуть к выбору улицы
            await context.set_state(Registration.fill_street)
            kb = get_streets_kb(streets_list)
            await message.edit("Такой адрес уже есть в базе. Начните заново и выберите другой адрес:", attachments=[kb])
    else:
        await context.set_state(Registration.fill_house_number)
        await message.edit("Пожалуйста, введите номер дома заново:",attachments=[])



@router.message_callback(
    F.callback.payload == 'Начать сначала',
    Registration.fill_street,
    Registration.street_confirming,
    Registration.fill_house_number,
    Registration.confirm_house_number
)
async def restart_registration(event: MessageCreated, context: MemoryContext):
    message = event.message
    await event.message.delete() #Удалить сообщение
    await context.clear()
    await context.set_state(Registration.fill_street)

    await context.update_data(name=event.from_user.full_name)
    await message.answer("Выберите улицу:", attachments=[get_streets_kb(streets_list)])


@router.message_callback(F.callback.payload == 'Сообщить о сборе мусора')
async def ask_status(event: MessageCallback):
    message = event.message
    await message.edit("Мусор собран?", attachments=[get_yes_no_trash_kb()])


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
        await message.edit(
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
        await message.edit("Нет записей для редактирования.")
        return

    if not await can_edit_record(record["report_date"]):
        week_range = get_week_range_text(record["report_date"])
        await message.edit(
            f"❌ Нельзя изменить запись за неделю\n{week_range}:\nона старше текущей календарной недели."
        )
        return

    week_range = get_week_range_text(record["report_date"])
    new_answer = record['answer']
    if new_answer == 'Да':
        symb = '✅️'
    else :
        symb = '❌️'


    await message.edit(
        f"Текущая запись за неделю\n{week_range}:\n\n«{symb}{record['answer']}».\n\nВыберите новый статус:",
        attachments=[get_yes_no_trash_kb()]
    )

@router.message_created(Commands.count_payments)
async def count_payments(event: MessageCreated, context: MemoryContext):
    message = event.message
    text = message.body.text
    result = count_payments(text)

    await message.answer(f'Результат: {result} Руб.')

    #Очистить состояние
    await context.clear()

@router.message_created(Commands.create_a_newsletter)
async def handle_message_newsletter(event: MessageCreated, context: MemoryContext):
    message = event.message
    text = message.body.text

    await context.update_data(message_for_news_letter=text)

    await message.answer(
        f'Сообщение пользователям:\n\n"{text}"\n\n'
        f'Выполнить рассылку данного сообщения?',
        attachments=[get_yes_no_kb()]
    )
    await context.set_state(Commands.create_a_newsletter_confirm)

@router.message_callback(Commands.create_a_newsletter_confirm,F.callback.payload.in_(['Да','Нет']))
async def handle_confirm_newsletter(event: MessageCallback, context: MemoryContext):
    message = event.message
    payload = event.callback.payload

    # Получили из памяти (FSM)
    data = await context.get_data()
    message_for_news_letter = data.get('message_for_news_letter')

    if payload == 'Нет':
        await message.edit(
            'Рассылка пользователям отменена',
            attachments=[]
        )
    else:
        await message.edit(
            'Рассылка выполняется...',
            attachments=[]
        )
        await mailing_newsletter(event,message_for_news_letter)

    await context.clear()




@router.message_callback(F.callback.payload.in_(["Полная", "Да", "Нет","Без ответа"]),Commands.get_statistic)
async def handle_stat_buttons(event:MessageCallback,context : MemoryContext):
    message = event.message
    # Проверка прав админа (обязательно и тут!)
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS :
        await message.edit("❌ Доступ запрещён")
        return

    # Вызываем статистику. Передаём event., потому что get_statistic ждёт MessageCreated
    await get_statistic(message=message, filter_type=event.callback.payload)

    await context.clear()

@router.message_callback(F.callback.payload == 'Повторить рассылку')
async def handle_command_repeat_mailing(event:MessageCallback,context:MemoryContext):
    message = event.message

    # Проверка прав админа (обязательно и тут!)
    if event.from_user.user_id not in ADMINS_IDS and event.from_user.user_id not in SUB_ADMINS_IDS:
        await message.edit("❌ Доступ запрещён")
        return

    await context.set_state(Commands.confirm_repeat_mailing)
    await message.edit(
        "Вы уверены, что хотите совершить рассылку всем неответившим пользователям?",
        attachments=[get_yes_no_kb()]
    )

@router.message_callback(Commands.confirm_repeat_mailing,F.callback.payload.in_(['Да','Нет']))
async def handle_confirm_repeat_mailing(event: MessageCallback, context: MemoryContext):

    message = event.message

    if event.callback.payload == 'Нет':
        await message.edit('Выберите доступные команды:',attachments=[get_commands_kb()])
    else:
        await send_weekly_reminder_to_users(event)


# Эхо-хендлер — только если пользователь в каком-то состоянии (например, в форме)
# Если ты хочешь вообще отключить эхо — просто удали этот хендлер
@router.message_created(Registration.fill_street,
    Registration.street_confirming,
    Registration.fill_house_number,
    Registration.confirm_house_number)
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

# ГЛАВНЫЙ ХЕНДЛЕР-СТРАЖ — только для сообщений, когда пользователь НЕ в FSM
@router.message_created()
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
        kb = get_streets_kb(streets_list)
        await message.answer(
            f"Привет, {user.first_name}!\nПредлагаю познакомиться!\n\nВыберите улицу:",
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

async def setup_bot_commands():

    await bot.set_my_commands(
        BotCommand(name="stat", description="Получить статистику"),
        BotCommand(name="commands", description="Показать доступные команды"),
        BotCommand(name="payments", description="Платежи(админ)"),
        BotCommand(name="newsletter", description="Новостная рассылка(админ)"),
                              )

async def main():
    await init_db()
    dp.include_routers(router)
    await setup_bot_commands()
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

    scheduler.add_job(
        users_to_new_week,
        CronTrigger(hour=15, minute=0, day_of_week='mon'),  # day_of_week='mon'
        id='create_users_to_new_week',
        replace_existing=True  # <-- если задача уже есть, заменит её, а не добавит новую
    )  
    await users_to_new_week()
    scheduler.start()
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

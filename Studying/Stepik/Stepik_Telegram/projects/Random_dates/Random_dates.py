# from icrawler.builtin import GoogleImageCrawler
import asyncio
import  random
import pickle
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.types import ContentType
from aiogram import F
from random import randint
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN


FILE_URL = None

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
# google_crawler = GoogleImageCrawler(storage={'root_dir':'..'})


# def get_photo_by_event(event):
#     if 'День' in event :
#         event = event[event.index('День')+1:]
#     google_crawler.crawl(keyword=event,max_num=1)

list_of_buttons = []

# Создаем объекты кнопок
buttons = [KeyboardButton(text=f'{index}') for index in range(1,32)]
print(buttons)

keyboard = ReplyKeyboardMarkup(keyboard=[buttons[0:5],
                                         buttons[5:10],
                                         buttons[10:15],
                                         buttons[15:20],
                                         buttons[20:25],
                                         buttons[25:30],
                                         [buttons[-1]]],
                               resize_keyboard=True)



def read_date_events()->dict[str,list]:
    with open('holidays_dates.txt', encoding='utf-8') as file:
        dictionary = {}
        sep = '-'
        for line in file:
            if line[0].isdigit():
                line = line.strip('\n')
                date = line[:line.index('-')-1]
                line = line[line.index('-')+2:]
                if not dictionary.get(date):
                    dictionary[date] = []
                dictionary[date].append(line)
    return dictionary


dictionary = read_date_events()
def get_date_event():
        date = random.choice(list(dictionary.keys()))
        day,month = date.split(' ')
        day = int(day)
        event_list = dictionary[date]
        event = random.choice(event_list)
        return day,month,event




#Количество попыток, доступных пользователю в игре
ATTEMPTS = 5

# Словарь, в котором будут храниться данные пользователей
users = {}

# Начальный словарь - шаблон данны пользователя
user_dict = {'in_game': False,
        'secret_day': None,
        'secret_month':None,
        'event':None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}

positive_answers = ['да', 'давай', 'сыграем', 'игра','играть', 'хочу играть','ладно','хорошо','ок','давайте','хочу','уговорил']
negative_answers = ['нет', 'не', 'не хочу', 'не буду']



def read_users_data():
    with open('users_data', 'rb') as input_file:
        data_load = pickle.load(input_file)
        return data_load

def write_users_data():
    with open('users_data', 'wb') as output_file:
        pickle.dump(users,output_file)
users = read_users_data()


#Получение случайного номера
def get_random_number() -> int:
    return randint(1,100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = user_dict
        try:
            await bot.send_message(852757379,f'Ура! У нас новый пользователь: {user_id}:{message.from_user.username}')
        except Exception:
            print(Exception)
    await message.answer( 'Привет!\nДавайте сыграем в игру "Угадай дату"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help')
    write_users_data()


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        f'Правила игры:\n\nЯ загадываю событие - праздник, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила\n'
        f'/stat - посмотреть статистику\n'
        f'игры и список команд\n'
        f'/sur - сдаться \n'
        f'/cancel - выйти из игры\n\nДавай сыграем?'
    )

@dp.message(Command(commands=['stat']))
async def process_stat_command(message:Message):
    user_id = message.from_user.id
    await message.answer(
        f'Всего игр сыграно: {users[user_id]["total_games"]}\n'
        f'Игр выиграно: {users[user_id]["wins"]}'
    )

@dp.message(Command(commands=['sur']))
async def process_stat_command(message:Message):
    user_id = message.from_user.id
    if users[user_id]['in_game']:
        users[user_id]['in_game'] = False
        await message.answer(
            f'Очень жаль, что вы сдаетесь. Рано или поздно Вы победите!'
        )
    else:
        await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?'
        )
    write_users_data()


@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message:Message):
    user_id = message.from_user.id
    if users[user_id]['in_game']:
        users[user_id]['in_game'] = False
        await message.answer(
            'Вы вышли из игры. Если захотите сыграть '
            'снова - напишите об этом'
        )
    else:
        await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?'
        )
    write_users_data()

@dp.message(F.text.lower().in_(positive_answers))
async def process_positive_answer(message:Message):
    user_id = message.from_user.id
    if not users[user_id]['in_game']:
        users[user_id]['in_game'] = True
        await process_generate_question(message,user_id,first_generate=True)
        # users[user_id]['secret_day'],users[user_id]['secret_month'], users[user_id]['event'] = get_date_event()
        # users[user_id]['attempts'] = ATTEMPTS
        # get_photo_by_event(user['event'])
        # await message.answer(
        #     'Ура!\nЯ загадал событие, попробуй угадать!\n\n'
        #     f'В какой день {users[user_id]["secret_month"].capitalize()} празднуется:\n'
        #     f'{users[user_id]["event"]}'
        # )
    else:
        await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /cancel, /stat и /sur'
        )
        await asyncio.sleep(2)
        await process_ask_again(message, user_id)

    write_users_data()

async def process_generate_question(message,user_id,first_generate = None):
    users[user_id]['secret_day'], users[user_id]['secret_month'], users[user_id]['event'] = get_date_event()
    users[user_id]['attempts'] = ATTEMPTS
    # get_photo_by_event(user['event'])
    start_message_text = ['Ура!\nЯ загадал событие, попробуй угадать!\n\n'
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}']
    next_message_text = ['Я загадал следующее событие, попробуй угадать!\n\n'
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}']

    #Если это не первый вопрос, тогда добавляется ожидание 2 секунды
    if first_generate is None:
        await asyncio.sleep(2)
        await message.answer(
            next_message_text[0],
            parse_mode='html',
            reply_markup=keyboard
        )
    else:
        await message.answer(
            start_message_text[0],
            parse_mode='html',
            reply_markup=keyboard
        )

async def process_ask_again(message,user_id):
    await message.answer(
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}',
        parse_mode='html',
        reply_markup=keyboard
    )



@dp.message(F.text.lower().in_(negative_answers))
async def process_negative_answer(message:Message):
    user_id = message.from_user.id
    if not users[user_id]['in_game']:
        await message.answer(
            'Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом'
        )
    else:
        await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /cancel, /stat и /sur'
        )
        await asyncio.sleep(2)
        await process_ask_again(message, user_id)


@dp.message(lambda x: x.text and x.text.isdigit() and 1<= int(x.text) <= 31)
async def process_numbers_answer(message:Message):
    user_id = message.from_user.id
    day_answer = int(message.text)
    if users[user_id]['in_game']:
        if users[user_id]['secret_day'] == day_answer:
            # users[user_id]['in_game'] = False
            users[user_id]['total_games'] += 1
            users[user_id]['wins'] += 1
            await message.answer(
                'Ура!!! Вы угадали день!\n\n'
                f'<b>{users[user_id]["secret_day"]} {users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
                f'{users[user_id]["event"]}\n\n',
                parse_mode='html'
                # 'Может, сыграем еще?'
            )

            #Продолжение игры после правильного ответа
            await process_generate_question(message,user_id)

        elif day_answer < users[user_id]['secret_day'] :
            users[user_id]['attempts'] -= 1
            if users[user_id]['attempts'] != 0:
                await message.answer(
                    'Это событие празднуется <b>позже</b>,\n'
                    'попробуйте другой вариант',
                    parse_mode='html'
                                     )
            else:
                await message.answer(
                    'Это событие празднуется <b>позже</b>',parse_mode='html'
                )
        elif day_answer > users[user_id]['secret_day']:
            users[user_id]['attempts'] -= 1
            if users[user_id]['attempts'] != 0:
                await message.answer(
                    'Это событие празднуется <b>раньше</b>,\n'
                    'попробуйте другой вариант',
                    parse_mode = 'html'
                )
            else:
                await message.answer(
                    'Это событие празднуется <b>раньше</b>',
                    parse_mode='html'
                )

        if users[user_id]['attempts'] == 0:
            # users[user_id]['in_game'] = False
            users[user_id]['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\n'
                f'<b>{users[user_id]["secret_day"]} {users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
                f'{users[user_id]["event"]}\n\n',
                parse_mode='html'
                # f'Давайте сыграем еще?'
            )
            #Продолжение игры после неправильного ответа
            await process_generate_question(message,user_id)

    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')
    write_users_data()

# @dp.message()
# async def process_date(message:Message):
#     date, event = get_date_event()
#     await message.answer(
#         'В какой день празднуется это событие:\n'
#         f'{event}'
#     )
# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def process_other_answers(message: Message):
    user_id = message.from_user.id
    if users[user_id]['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 31'
        )
        await asyncio.sleep(2)
        await process_ask_again(message,user_id)
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )
dp.run_polling(bot)



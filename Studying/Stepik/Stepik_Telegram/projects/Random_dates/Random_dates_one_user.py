# from icrawler.builtin import GoogleImageCrawler

import  random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from random import randint
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN
#

FILE_URL = None
# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
# google_crawler = GoogleImageCrawler(storage={'root_dir':'..'})


# def get_photo_by_event(event):
#     if 'День' in event :
#         event = event[event.index('День')+1:]
#     google_crawler.crawl(keyword=event,max_num=1)


def read_date_events()->dict[str,list]:
    with open('dates.txt') as file:
        dictionary = {}
        for line in file:
            if line[0].isdigit():
                line = line.strip('\n')
                date = line[:line.index('–')-1]
                line = line[line.index('–')+2:]
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

# Словарь, в котором будут храниться данные пользователя
user = {'in_game': False,
        'secret_day': None,
        'secret_month':None,
        'event':None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}

positive_answers = ['да', 'давай', 'сыграем', 'игра','играть', 'хочу играть','ладно','хорошо','ок','давайте','хочу','уговорил']
negative_answers = ['нет', 'не', 'не хочу', 'не буду']

#Получение случайного номера
def get_random_number() -> int:
    return randint(1,100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer( 'Привет!\nДавайте сыграем в игру "Угадай дату"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help')


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
    await message.answer(
        f'Всего игр сыграно: {user["total_games"]}\n'
        f'Игр выиграно: {user["wins"]}'
    )

@dp.message(Command(commands=['sur']))
async def process_stat_command(message:Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            f'Очень жаль, что вы сдаетесь. Рано или поздно Вы победите!'
        )
    else:
        await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?'
        )


@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message:Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            'Вы вышли из игры. Если захотите сыграть '
            'снова - напишите об этом'
        )
    else:
        await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?'
        )

@dp.message(F.text.lower().in_(positive_answers))
async def process_positive_answer(message:Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_day'],user['secret_month'], user['event'] = get_date_event()
        user['attempts'] = ATTEMPTS
        # get_photo_by_event(user['event'])
        await message.answer(
            'Ура!\nЯ загадал событие, попробуй угадать!\n\n'
            f'В какой день {user["secret_month"].capitalize()} празднуется:\n'
            f'{user["event"]}'
        )
    else:
        await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты'
            'и команды /cancel, /stat и /sur'
        )

@dp.message(F.text.lower().in_(negative_answers))
async def process_negative_answer(message:Message):
    if not user['in_game']:
        await message.answer(
            'Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом'
        )
    else:
        await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /cancel, /stat и /sur'
        )


@dp.message(lambda x: x.text and x.text.isdigit() and 1<= int(x.text) <= 31)
async def process_numbers_answer(message:Message):
    day_answer = int(message.text)
    if user['in_game']:
        if user['secret_day'] == day_answer:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer(
                'Ура!!! Вы угадали день!\n\n'
                f'{user["secret_day"]} {user["secret_month"].capitalize()} празднуется:\n'
                f'{user["event"]}\n\n'
                'Может, сыграем еще?'
            )

        elif day_answer < user['secret_day'] :
            user['attempts'] -= 1
            await message.answer('Это событие празднуется позже')
        elif day_answer > user['secret_day']:
            user['attempts'] -= 1
            await message.answer('Это событие празднуется раньше')

        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\n'
                f'{user["secret_day"]} {user["secret_month"].capitalize()} празднуется:\n'
                f'{user["event"]}\n\n'
                f'Давайте сыграем еще?'
            )
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')

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
    if user['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 31'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )
dp.run_polling(bot)
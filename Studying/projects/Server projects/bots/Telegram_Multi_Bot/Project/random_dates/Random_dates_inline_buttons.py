# from icrawler.builtin import GoogleImageCrawler
import asyncio
import logging
import  random
import pickle
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (Message,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove,
InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery)
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

#Логирование
logging.basicConfig(level=logging.DEBUG)

#Buttons
list_of_numbers = [InlineKeyboardButton(text=f'{index}',callback_data=f'{index}') for index in range(1,32)]
list_of_callback = [str(index) for index in range (1,32)]
yes_button = InlineKeyboardButton(text='Давай',callback_data='yes_button')
no_button = InlineKeyboardButton(text='Не хочу',callback_data='no_button')
good_button = InlineKeyboardButton(text='Хорошо',callback_data='good_button')

# Создаем объекты кнопок
kb_builder = InlineKeyboardBuilder()
kb_builder.add(*list_of_numbers)

yes_no_keyboard = InlineKeyboardMarkup(inline_keyboard=[[yes_button,no_button]])
bots_response_status = 'free'



# kb_builder.adjust(5)


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
        'wins': 0,
        'user_messages_ids':[],
        'bot_messages_ids':[]
             }

positive_answers = ['да', 'давай', 'сыграем', 'игра','играть', 'хочу играть','ладно','хорошо','ок','давайте','хочу','уговорил']
negative_answers = ['нет', 'не', 'не хочу', 'не буду']

async def remove_keyboard():
    await bot.send_message(852757379,f'',reply_markup=ReplyKeyboardRemove())



def read_users_data():
    with open('users_data', 'rb') as input_file:
        data_load = pickle.load(input_file)
        return data_load

def write_users_data():
    with open('users_data', 'wb') as output_file:
        pickle.dump(users,output_file)

users:dict = read_users_data()
for user in users:
    users[user]['bot_messages_ids'] = []
    users[user]['user_messages_ids'] = []


write_users_data()


async def one_time(user):
    await bot.send_message(user, 'Привет! Мы давно не играли', reply_markup=ReplyKeyboardRemove())



#Получение случайного номера
def get_random_number() -> int:
    return randint(1,100)




# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    user_id = message.from_user.id
    await save_users_message(user_id,message) # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id) #Удалить сообщение от бота

    if user_id not in users:
        users[user_id] = user_dict
        try:
            bot_msg = await bot.send_message(852757379,f'Ура! У нас новый пользователь: {user_id}:{message.from_user.username}')
        except Exception:
            print(Exception)
    bot_msg = await message.answer( 'Привет!\nДавайте сыграем в игру "Угадай дату"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help',
        reply_markup=yes_no_keyboard)

    await save_bot_message(user_id,bot_msg) # Сохраняем сообщение от бота
    await delete_message_from_user(user_id) # Удалить сообщения от пользователя
    write_users_data()


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id) #Удалить сообщение от бота

    bot_msg = await message.answer(
        f'Правила игры:\n\nЯ загадываю событие - праздник, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила\n'
        f'/stat - посмотреть статистику\n'
        f'игры и список команд\n'
        f'/sur - сдаться \n'
        f'/cancel - выйти из игры\n\nДавай сыграем?',
        reply_markup=yes_no_keyboard
    )
    await save_bot_message(user_id,bot_msg)#Сохранить сообщение от бота
    await delete_message_from_user(user_id)  # Удалить сообщения от пользователя


@dp.message(Command(commands=['stat']))
async def process_stat_command(message:Message):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id)  # Удалить сообщение от бота

    bot_msg = await message.answer(
        f'Всего игр сыграно: {users[user_id]["total_games"]}\n'
        f'Игр выиграно: {users[user_id]["wins"]}'
    )

    await save_bot_message(user_id,bot_msg) #Сохранить сообщение от бота
    await delete_message_from_user(user_id)  # Удалить сообщения от пользователя

    await asyncio.sleep(3)
    if users[user_id]['in_game']:
        await process_ask_again(message, user_id)
    else:
        await bot.edit_message_text(chat_id=user_id,message_id=bot_msg.message_id,text=
            f'Всего игр сыграно: {users[user_id]["total_games"]}\n'
            f'Игр выиграно: {users[user_id]["wins"]}\n'
            f'Давайте сыграем?\n',
            reply_markup=yes_no_keyboard
        )





@dp.message(Command(commands=['sur']))
async def process_stat_command(message:Message):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id)  # Удалить сообщение от бота

    if await have_callback_message(user_id):
        await delete_message_from_bot(user_id)
    if users[user_id]['in_game']:
        users[user_id]['in_game'] = False
        bot_msg = await message.answer(
            f'Очень жаль, что вы сдаетесь. Рано или поздно Вы победите!\n'
            f'Чтобы начать игру нажмите кнопку или напишите мне любое сообщение.\n\n'
            f'Может быть поиграем ещё?',
            reply_markup=yes_no_keyboard
        )

    else:
        bot_msg = await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?',
            reply_markup=yes_no_keyboard
        )
    await delete_message_from_user(user_id)  # Удалить сообщения от пользователя
    await save_bot_message(user_id, bot_msg)  # Сохранить сообщение от бота

    write_users_data()


@dp.message(Command(commands=['cancel']))
async def process_cancel_command(message:Message):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id)  # Удалить сообщение от бота


    if users[user_id]['in_game']:
        users[user_id]['in_game'] = False
        bot_msg = await message.answer(
            'Вы вышли из игры. Если захотите сыграть снова - '
            'нажмите кнопку или напишите мне любое сообщение.\n\n'
            'Может быть продолжим игру?',
            reply_markup=yes_no_keyboard
            # reply_markup=InlineKeyboardMarkup(inline_keyboard=[[good_button]])
        )
    else:
        bot_msg = await message.answer(
            'А мы и так с вами не играем. '
            'Может, сыграем разок?',
            reply_markup=yes_no_keyboard
        )
    await delete_message_from_user(user_id)  # Удалить сообщения от пользователя
    await save_bot_message(user_id, bot_msg)  # Сохранить сообщение от бота

    write_users_data()

@dp.callback_query(F.data == 'good_button')
async def process_good_button(callback:CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer()
    await delete_message_from_bot(user_id)



@dp.callback_query(F.data == 'yes_button')
async def process_positive_answer(callback:CallbackQuery):
    user_id = callback.from_user.id
    users[user_id]['current_message_id'] = callback.message.message_id
    message = callback.message
    await delete_message_from_bot(user_id) #Удалить сообщение от бота

    await callback.answer()
    if not users[user_id]['in_game']:
        users[user_id]['in_game'] = True
        await process_generate_question(message,user_id,first_generate=True)
    else:
        msg_warning = await  message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /help, /stat, /sur и /cancel '
            'которые находятся в кнопке <b>Menu</b>',
            parse_mode='html'

        )

        await asyncio.sleep(5)
        await save_bot_message(user_id,msg_warning)
        await delete_message_from_bot(user_id)  # Удалить сообщение от бота
        await process_ask_again(message, user_id)
    write_users_data()

async def process_generate_question(message,user_id,first_generate = None):

    users[user_id]['secret_day'], users[user_id]['secret_month'], users[user_id]['event'] = get_date_event()
    users[user_id]['attempts'] = ATTEMPTS


    start_message_text = ['Ура!\nЯ загадал событие, попробуй угадать!\n\n'
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}']

    next_message_text = ['Я загадал следующее событие, попробуй угадать!\n\n'
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}']

    #Если это не первый вопрос, тогда добавляется ожидание 2 секунды
    if first_generate is None:
        await asyncio.sleep(2)
        bot_msg = await message.answer(
            next_message_text[0],
            parse_mode='html',
            reply_markup=kb_builder.as_markup()
        )
    else:
        bot_msg = await message.answer(
            start_message_text[0],
            parse_mode='html',
            reply_markup=kb_builder.as_markup()
        )
    await save_bot_message(user_id,bot_msg) #Сохранить сообщение от бота
    print('Proccess generate question',message.message_id)

async def process_ask_again(message,user_id):
    bot_msg = await message.answer(
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}',
        parse_mode='html',
        reply_markup=kb_builder.as_markup()
    )
    await save_bot_message(user_id,bot_msg)



@dp.callback_query(F.data == 'no_button')
async def process_negative_answer(callback:CallbackQuery):
    message = callback.message
    user_id = callback.from_user.id
    users[user_id]['current_message_id'] = callback.message.message_id
    await delete_message_from_bot(user_id)  # Удалить сообщение от бота

    await callback.answer()
    if not users[user_id]['in_game']:
        bot_msg = await message.answer(
            'Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом',
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[good_button]])
        )
    else:
        bot_msg = await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /help, /stat, /cancel и /sur '
            'которые находятся в кнопке <b>Menu</b>'
        )
    await save_bot_message(user_id,bot_msg) #Сохранить сообщение от бота
    await asyncio.sleep(2)
    # await delete_message_from_bot(user_id)  # Удалить сообщение от бота


    if users[user_id]['in_game']:
        await process_ask_again(message, user_id)


@dp.callback_query(F.data.in_(*[list_of_callback]))
async def process_numbers_answer(callback:CallbackQuery):
    user_id = callback.from_user.id
    day_answer = int(callback.data)
    message = callback.message
    users[user_id]['current_message_id'] = message.message_id
    if users[user_id]['in_game']:
        if users[user_id]['secret_day'] == day_answer:
            users[user_id]['total_games'] += 1
            users[user_id]['wins'] += 1
            await callback.answer()
            await message.answer(
                'Ура!!! Вы угадали день!\n\n'
                f'<b>{users[user_id]["secret_day"]} {users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
                f'{users[user_id]["event"]}\n\n',
                parse_mode='html',
                show_alert=True,
            )
            await asyncio.sleep(2)
            await callback.message.delete()

            #Продолжение игры после правильного ответа
            await process_generate_question(message,user_id)

        elif day_answer < users[user_id]['secret_day'] :
            users[user_id]['attempts'] -= 1
            if users[user_id]['attempts'] != 0:
                await callback.answer(
                    text=f'Ваш ответ: {callback.data} {users[user_id]["secret_month"]}.\n\nЭто событие празднуется позже,\n'
                        'попробуйте другой вариант',
                    parse_mode='html',
                    show_alert=True,
                                     )
            else:
                await callback.answer(
                    'Это событие празднуется позже',parse_mode='html'
                )

        elif day_answer > users[user_id]['secret_day']:
            users[user_id]['attempts'] -= 1
            if users[user_id]['attempts'] != 0:
                await callback.answer(
                    f'Ваш ответ: {callback.data} {users[user_id]["secret_month"]}.\n\nЭто событие празднуется раньше,\n'
                    'попробуйте другой вариант',
                    parse_mode = 'html',
                    show_alert=True,

                )
            else:
                await callback.answer(
                    'Это событие празднуется раньше',
                    parse_mode='html',
                    show_alert=True,

                )



        if users[user_id]['attempts'] == 0:
            # users[user_id]['in_game'] = False
            await callback.message.delete()
            users[user_id]['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\n'
                f'<b>{users[user_id]["secret_day"]} {users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
                f'{users[user_id]["event"]}\n\n',
                parse_mode='html',
                show_alert=True
                # f'Давайте сыграем еще?'
            )

            #Продолжение игры после неправильного ответа
            await asyncio.sleep(3)
            await process_generate_question(message,user_id)


    else:
        await message.answer('Мы еще не играем. Хотите сыграть?',reply_markup=yes_no_keyboard)
    await callback.answer()
    write_users_data()

async def have_callback_message(user_id):
    if users[user_id]['current_message_id'] != 0:
        return True
    else:
        return False

async def save_bot_message(user_id,message):
    users[user_id]['bot_messages_ids'].append(message.message_id)  # Добавляем новое сообщение в список
    logging.info(f'Записано сообщение бота : {message.message_id} от бота')

async def save_users_message(user_id, message):
    users[user_id]['user_messages_ids'].append(message.message_id)  # Добавляем новое сообщение в список
    logging.info(f'Записано сообщение пользователя : {message.message_id}')


async def delete_message_from_bot(user_id):
    message_ids_list: list = users[user_id]['bot_messages_ids']
    logging.info(f'Сообщения бота : {message_ids_list}')
    if len(message_ids_list) >0 :
        users[user_id]['bot_messages_ids'] = []
        logging.info(f'Сообщения бота удалены : {message_ids_list}')
        await bot.delete_messages(chat_id=user_id, message_ids=message_ids_list)



async def delete_message_from_user(user_id):
    message_ids_list: list = users[user_id]['user_messages_ids']
    logging.info(f'Сообщения пользователя : {message_ids_list}')
    if len(message_ids_list) > 0:
        users[user_id]['user_messages_ids'] = []
        logging.info(f'Сообщения пользователя удалены : {message_ids_list}')
        await bot.delete_messages(chat_id=user_id,message_ids=message_ids_list)



# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def process_other_answers(message: Message):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_user(user_id)  # Удалить сообщения от пользователя
    await delete_message_from_bot(user_id) # Удалить сообщения от бота

    # if await have_callback_message(user_id):
    #     await delete_message_from_bot(user_id)

    if users[user_id]['in_game']:
        msg_warning = await message.answer(
            'Мы же сейчас с вами играем. '
            'Выбирайте, пожалуйста, числа на предложенной клавиатуре'
        )
        await save_bot_message(user_id, msg_warning)
        await asyncio.sleep(1)
        # await delete_message_from_bot(user_id)  # Удалить сообщение от бота

        # await bot.delete_message(user_id,msg_warning.message_id) # Удалить сообщение от бота
        await process_ask_again(message,user_id)

    else:
        msg_warning = await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?',
            reply_markup=yes_no_keyboard
        )
        await save_bot_message(user_id,msg_warning) #Сохранить сообщение от боты
dp.run_polling(bot)



from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.types import (Message,ReplyKeyboardRemove,CallbackQuery)
from aiogram.filters import Command
from aiogram import F
import asyncio
import logging
import random
from aiogram import Router
from random import randint
from ..data.users_data import *
from ..keyboards.keyboards import *
import os

current_path = os.path.dirname(os.path.abspath(__file__))


#Инициализируем роутер уровня модуля
router = Router()

users_in_game=[]







def read_date_events()->dict[str,list]:
    with open(current_path+'/holidays_dates.txt', encoding='utf-8') as file:
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



positive_answers = ['да', 'давай', 'сыграем', 'игра','играть', 'хочу играть','ладно','хорошо','ок','давайте','хочу','уговорил']
negative_answers = ['нет', 'не', 'не хочу', 'не буду']

async def remove_keyboard():
    await router.send_message(852757379,f'',reply_markup=ReplyKeyboardRemove())

class IsPlayer(BaseFilter):
    def __init__(self, users_in_game:list[int])->None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.users_in_game = users_in_game

    async def __call__(self,message:Message)->bool:
        return message.from_user.id in self.users_in_game

async def one_time(user):
    await router.send_message(user, 'Привет! Мы давно не играли', reply_markup=ReplyKeyboardRemove())



#Получение случайного номера
def get_random_number() -> int:
    return randint(1,100)




@router.message(F.text == guess_date_button.text)
async def process_guess_date_command(message:Message,bot):
    user_id = message.from_user.id

    # Добавить игроку статус Игра
    if user_id not in users_in_game:
        users_in_game.append(user_id)

    await delete_message_from_bot(user_id,bot) #Удалить сообщение от бота

    if user_id not in users:
        users[user_id] = user_dict

    bot_msg = await message.answer( 'Играем в "Угадай дату"\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help',
        reply_markup = exit_game_keyboard
)

    await save_bot_message(user_id,bot_msg) # Сохраняем сообщение от бота
    await delete_message_from_user(user_id,bot) # Удалить сообщения от пользователя


    users[user_id]['current_message_id'] = message.from_user.id

    if not users[user_id]['in_game']:
        users[user_id]['in_game'] = 1
        await process_generate_question(message, user_id)
    else:
        await process_ask_again(message, user_id)
    update_users_data(user_id)



# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']),IsPlayer(users_in_game))
async def process_help_command(message: Message,bot):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id,bot) #Удалить сообщение от бота

    bot_msg = await message.answer(
        f'Правила игры:\n\nЯ загадываю событие - праздник, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        f'попыток\n\nДоступные команды:\n/help - правила\n'
        f'/stat - посмотреть статистику\n'
        f'игры и список команд\n'
        f'/sur - сдаться \n'
        f'/cancel - выйти из игры\n\n',
        reply_markup=exit_game_keyboard
    )
    await save_bot_message(user_id,bot_msg)#Сохранить сообщение от бота
    await delete_message_from_user(user_id,bot)  # Удалить сообщения от пользователя
    # #await asyncio.sleep(3)
    await process_ask_again(message,user_id)

@router.message(Command(commands=['stat']),IsPlayer(users_in_game))
async def process_stat_command(message:Message,bot):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id,bot)  # Удалить сообщение от бота

    bot_msg = await message.answer(
        f'Всего игр сыграно: {users[user_id]["total_games"]}\n'
        f'Игр выиграно: {users[user_id]["wins"]}',
        reply_markup = exit_game_keyboard
    )

    await save_bot_message(user_id,bot_msg) #Сохранить сообщение от бота
    await delete_message_from_user(user_id,bot)  # Удалить сообщения от пользователя
    await process_ask_again(message, user_id) #Задать вопрос заново





@router.message(Command(commands=['sur']),IsPlayer(users_in_game))
async def process_stat_command(message:Message,bot):
    user_id = message.from_user.id

    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id,bot)  # Удалить сообщение от бота

    if users[user_id]['in_game']:
        users[user_id]['in_game'] = 0

        # Удалить игроку статус Игра
        if user_id in users_in_game:
            users_in_game.pop(users_in_game.index(user_id))

        bot_msg = await message.answer(
            f'Очень жаль, что вы сдаетесь. Рано или поздно Вы победите!\n'
            f'Чтобы начать игру нажмите кнопку или напишите мне любое сообщение.\n\n'
            f'Может быть поиграем ещё?',
            reply_markup=yes_no_keyboard
        )
        await save_bot_message(user_id, bot_msg)

    await delete_message_from_user(user_id,bot)  # Удалить сообщения от пользователя
      # Сохранить сообщение от бота

    update_users_data(user_id)


@router.message(Command(commands=['cancel']),IsPlayer(users_in_game))
async def process_cancel_command(message:Message,bot):
    user_id = message.from_user.id


    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_bot(user_id,bot)  # Удалить сообщение от бота


    if users[user_id]['in_game']:
        users[user_id]['in_game'] = 0

        # Удалить игроку статус Игра
        if user_id in users_in_game:
            users_in_game.pop(users_in_game.index(user_id))

        bot_msg = await message.answer(
            'Вы вышли из игры. Если захотите сыграть снова - '
            'нажмите кнопку или напишите мне любое сообщение.\n\n'
            'Может быть продолжим игру?',
            reply_markup=yes_no_keyboard
        )
        await save_bot_message(user_id, bot_msg)  # Сохранить сообщение от бота
    await delete_message_from_user(user_id,bot)  # Удалить сообщения от пользователя


    update_users_data(user_id)

@router.callback_query(F.data == 'yes_button')
async def process_positive_answer(callback:CallbackQuery,bot):
    user_id = callback.from_user.id
    users[user_id]['current_message_id'] = callback.message.message_id
    message = callback.message
    await delete_message_from_bot(user_id,bot) #Удалить сообщение от бота

    await callback.answer()
    if not users[user_id]['in_game']:
        users[user_id]['in_game'] = True
        # Добавить игроку статус Игра
        if user_id not in users_in_game:
            users_in_game.append(user_id)

        await process_generate_question(message,user_id)
    else:
        msg_warning = await  message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на даты '
            'и команды /help, /stat, /sur и /cancel '
            'которые находятся в кнопке Menu',
            parse_mode='html',
            reply_markup=exit_game_keyboard

        )

        #await asyncio.sleep(5)
        await save_bot_message(user_id,msg_warning)
        await delete_message_from_bot(user_id,bot)  # Удалить сообщение от бота
        await process_ask_again(message, user_id)
    update_users_data(user_id)

async def process_generate_question(message,user_id):

    users[user_id]['secret_day'], users[user_id]['secret_month'], users[user_id]['event'] = get_date_event()
    users[user_id]['attempts'] = ATTEMPTS


    start_message_text = ['Я загадал событие, попробуй угадать!\n\n']

    question_message_text = [f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}']

    bot_msg = await message.answer(
        start_message_text[0],
        parse_mode='html',
        reply_markup=exit_game_keyboard
    )
    await save_bot_message(user_id, bot_msg)
    #Если это не первый вопрос, тогда добавляется ожидание 2 секунды
    #await asyncio.sleep(2)

    bot_msg = await message.answer(
        question_message_text[0],
        parse_mode='html',
        reply_markup=kb_builder.as_markup()
    )
    await save_bot_message(user_id, bot_msg)  # Сохранить сообщение от бота

    print('Proccess generate question',message.message_id)

async def process_ask_again(message,user_id):
    bot_msg = await message.answer(
        f'В какой день <b>{users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
        f'{users[user_id]["event"]}',
        parse_mode='html',
        reply_markup=kb_builder.as_markup()
    )
    await save_bot_message(user_id,bot_msg)



@router.callback_query(F.data == 'no_button')
async def process_negative_answer(callback:CallbackQuery,bot):
    message = callback.message
    user_id = callback.from_user.id
    users[user_id]['current_message_id'] = callback.message.message_id
    await delete_message_from_bot(user_id,bot)  # Удалить сообщение от бота
    # Удалить игроку статус Игра
    if user_id  in users_in_game:
        users_in_game.pop(users_in_game.index(user_id))

    await callback.answer()
    await message.answer('Очень жаль, возвращайтесь')
    await message.answer('Выберите команду:',reply_markup=start_keyboard)
    #await asyncio.sleep(2)


@router.callback_query(F.data.in_(*[list_of_callback]),IsPlayer(users_in_game))
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
                reply_markup=exit_game_keyboard
            )
            #await asyncio.sleep(2)
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
            await callback.message.delete()
            users[user_id]['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\n'
                f'<b>{users[user_id]["secret_day"]} {users[user_id]["secret_month"].capitalize()}</b> празднуется:\n'
                f'{users[user_id]["event"]}\n\n',
                parse_mode='html',
                show_alert=True,
                reply_markup=exit_game_keyboard
            )

            #Продолжение игры после неправильного ответа
            #await asyncio.sleep(3)
            await process_generate_question(message,user_id)

    await callback.answer()
    update_users_data(user_id)


async def save_bot_message(user_id,message):
    users[user_id]['bot_messages_ids'].append(message.message_id)  # Добавляем новое сообщение в список
    logging.info(f'Записано сообщение бота : {message.message_id} от бота')

async def save_users_message(user_id, message):
    users[user_id]['user_messages_ids'].append(message.message_id)  # Добавляем новое сообщение в список
    logging.info(f'Записано сообщение пользователя : {message.message_id}')


async def delete_message_from_bot(user_id,bot):
    message_ids_list: list = users[user_id]['bot_messages_ids']
    logging.info(f'Сообщения бота : {message_ids_list}')
    if len(message_ids_list) >0 :
        users[user_id]['bot_messages_ids'] = []
        logging.info(f'Сообщения бота удалены : {message_ids_list}')
        await bot.delete_messages(chat_id=user_id, message_ids=message_ids_list)



async def delete_message_from_user(user_id,bot):
    message_ids_list: list = users[user_id]['user_messages_ids']
    logging.info(f'Сообщения пользователя : {message_ids_list}')
    if len(message_ids_list) > 0:
        users[user_id]['user_messages_ids'] = []
        logging.info(f'Сообщения пользователя удалены : {message_ids_list}')
        await bot.delete_messages(chat_id=user_id,message_ids=message_ids_list)

@router.message(IsPlayer(users_in_game),F.text==exit_game_button.text)
async def process_exit_game(message:Message,bot,is_start=None):
    print("ВЫХОДИМ!!!")

    user_id = message.from_user.id
    if users[user_id]['in_game']:
        users[user_id]['in_game'] = 0

        # Удалить игроку статус Игра
        if user_id in users_in_game:
            users_in_game.pop(users_in_game.index(user_id))
    if is_start == None:
        await message.answer('Вы вышли из игры')
        await message.answer('Выберите команду:',reply_markup=start_keyboard)
    else:
        pass
    await delete_message_from_bot(user_id,bot)
    update_users_data(user_id)


# Этот хэндлер будет срабатывать на остальные любые сообщения
@router.message(IsPlayer(users_in_game))
async def process_other_answers(message: Message,bot):
    user_id = message.from_user.id
    await save_users_message(user_id, message)  # Сохранить сообщение от пользователя
    await delete_message_from_user(user_id,bot)  # Удалить сообщения от пользователя
    await delete_message_from_bot(user_id,bot) # Удалить сообщения от бота

    if users[user_id]['in_game']:
        msg_warning = await message.answer(
            'Мы же сейчас с вами играем. '
            'Выбирайте, пожалуйста, числа на предложенной клавиатуре',
            reply_markup=exit_game_keyboard
        )
        await save_bot_message(user_id, msg_warning)
        #await asyncio.sleep(1)
        await process_ask_again(message,user_id)



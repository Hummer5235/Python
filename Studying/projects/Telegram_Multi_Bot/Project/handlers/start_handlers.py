from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (Message)
from ..keyboards.keyboards import *
from .game_handlers import process_exit_game
from ..data.users_data import *
from .delete_messages.delete_game_messages import delete_message_from_bot


#Инициализируем роутер уровня модуля
router = Router()

read_users_data()


@router.message(Command(commands=['start']))
async def process_start_command(message:Message,bot):
    user_id = message.from_user.id

    #Записываем нового пользователя
    if user_id not in users:
        users[user_id] = user_dict
        try:
            bot_msg = await bot.send_message(852757379,f'Ура! У нас новый пользователь: {user_id}:{message.from_user.username}')
        except Exception:
            print(Exception)
        write_users_data(user_id)

    await delete_message_from_bot(user_id,bot) #Удаляем сообщения бота
    await process_exit_game(message,bot,True) #Выходим из игры

    await message.answer(
        text='Добро пожаловать! Выберите команду:',
        reply_markup=start_keyboard
    )


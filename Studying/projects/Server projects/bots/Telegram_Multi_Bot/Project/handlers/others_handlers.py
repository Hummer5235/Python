from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (Message,KeyboardButton,ReplyKeyboardMarkup)
from .delete_messages.delete_game_messages import delete_message_from_bot,delete_message_from_user
from .game_handlers import users_in_game, users, write_users_data
from ..keyboards.keyboards import *
from .game_handlers import process_exit_game



#Инициализируем роутер уровня модуля
router = Router()



@router.message()
async def process_other_answers(message:Message,bot):
    user_id = message.from_user.id
    user_name = message.from_user.username

    await delete_message_from_bot(user_id, bot)

    if user_id == 852757379:
        await message.answer(
            text='Выберите команду:',
            reply_markup=start_keyboard_admin
        )
    else:
        await message.answer(
            text = 'Выберите команду:',
            reply_markup=start_keyboard
        )


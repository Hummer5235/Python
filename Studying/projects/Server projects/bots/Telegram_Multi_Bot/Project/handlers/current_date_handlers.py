from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.types import (Message,KeyboardButton,ReplyKeyboardMarkup)
from aiogram import F
from aiogram import Router
from ..current_date.Main import main
from ..keyboards.keyboards import *
from .game_handlers import process_exit_game
from .delete_messages.delete_game_messages import delete_message_from_bot


#Инициализируем роутер уровня модуля
router = Router()




@router.message(F.text == current_date_button.text)
async def process_current_date_command(message:Message,bot):
    user_id = message.from_user.id
    await delete_message_from_bot(user_id,bot) #Удаляем сообщения бота
    fact = main()
    await message.answer(fact)
    await message.answer('Выберите команду:',reply_markup=start_keyboard)

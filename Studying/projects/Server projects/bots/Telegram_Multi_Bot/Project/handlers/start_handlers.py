from __future__ import annotations
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import BaseFilter
from ..keyboards.keyboards import *
from .game_handlers import process_exit_game
from ..data.users_data import *
from .delete_messages.delete_game_messages import delete_message_from_bot


#Инициализируем роутер уровня модуля
router = Router()
read_users_data()


class IsntUser(BaseFilter):
    def __init__(self, users:list[int])->None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.users = users

    async def __call__(self,message:Message)->bool:
        return message.from_user.id not in self.users


@router.message(IsntUser(users))
async def process_start_command(message:Message,bot):
    user = message.from_user
    user_id = user.id
    username = user.username

    try:
        bot_msg = await bot.send_message(852757379,f'Ура! У нас новый пользователь: {user_id}:{username}')
    except Exception:
        print(Exception)

    # Записываем нового пользователя
    write_users_data(user)


    await message.answer(
        text='Добро пожаловать! Выберите команду:',
        reply_markup=start_keyboard
    )


from aiogram import Router, F, Bot
from aiogram.filters import Command, BaseFilter
from aiogram.types import (Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from .delete_messages.delete_game_messages import delete_message_from_bot,delete_message_from_user

from ..keyboards.keyboards import *
from ..data.users_data import *

bot = Bot(token='6832374501:AAE9y0Q2S3l0tW51Pl916VSipog5l5uHhTM')

#Инициализируем роутер уровня модуля
router = Router()



class IsAdmin(BaseFilter):
    def __init__(self, admin_ids):
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self,message:Message)->bool:
        return message.from_user.id in self.admin_ids


class IsWaitingUser(BaseFilter):
    def __init__(self, waiting_users_dict: dict):
        self.waiting_users = waiting_users_dict

    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        return user_id in self.waiting_users and self.waiting_users[user_id]



@router.message(F.text == admin_button.text,IsAdmin(ADMIN_IDS))
async def process_admin_answers(message:Message,bot):

    await message.answer(
        text='Выберите команду:',
        reply_markup=main_keyboard_admin
    )

@router.message(F.text == message_for_users_button.text,IsAdmin(ADMIN_IDS))
async def process_ask_for_input(message:Message,bot):
    user_id = message.from_user.id
    user_name = message.from_user.username

    await delete_message_from_bot(user_id, bot)

    waiting_users[message.from_user.id] = True
    await message.answer(
        text='Что сообщить пользователям?',
        reply_markup= ReplyKeyboardMarkup(keyboard = [[back_button]],resize_keyboard= True)
    )


@router.message(F.text == back_button.text,IsAdmin(ADMIN_IDS))
async def process_admin_answers(message:Message,bot):
    user_id = message.from_user.id
    user_name = message.from_user.username

    await delete_message_from_bot(user_id, bot)

    await message.answer(
        text='Выберите команду:',
        reply_markup=start_keyboard_admin
    )

@router.message(F.text == message_for_users_button.text,IsAdmin(ADMIN_IDS))
async def process_admin_answers(message:Message,bot):
    user_id = message.from_user.id
    user_name = message.from_user.username

    await delete_message_from_bot(user_id, bot)

    await message.answer(
        text='Что сообщить пользователям?',
        reply_markup= ReplyKeyboardMarkup(keyboard = [[back_button]],resize_keyboard= True)
    )


@router.message(IsAdmin(ADMIN_IDS),IsWaitingUser(waiting_users))
async def handle_user_input(message: Message):
    user_id = message.from_user.id


    # Обрабатываем сообщение
    user_text = message.text
    await message.answer(
        f"Вы написали: {user_text}",
        reply_markup=ReplyKeyboardRemove()

    )
    # Сбрасываем флаг ожидания
    waiting_users[user_id] = False

    for user_id in users:
        await bot.send_message(user_id,user_text,parse_mode='html',reply_markup=start_keyboard)


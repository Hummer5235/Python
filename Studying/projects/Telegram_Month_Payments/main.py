import asyncio
import logging
from Count_month_payments import count_payments
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


#Логирование
logging.basicConfig(level=logging.DEBUG)

#Переменные
PAYMENTS_STATUS = False

#Кнопки
payments_button = KeyboardButton(
    text='Посчитать платежи',
    callback_data='payments_button'
)

#Клавиатура
start_keyboard = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    keyboard = [[payments_button]],
    resize_keyboard=True
)


# Создаем объекты кнопок
# kb_builder = InlineKeyboardBuilder()
# kb_builder.add(*list_of_numbers)

@dp.message(Command(commands=['start']))
async def process_payments_command(message:Message):
    user_id = message.from_user.id
    await message.answer(
        text ='Добро пожаловать! Выберите команду:',
        reply_markup=start_keyboard,
        )


@dp.message(F.text == 'Посчитать платежи')
async def process_payments_command(message:Message):
    global PAYMENTS_STATUS
    PAYMENTS_STATUS = True
    user_id = message.from_user.id
    await message.answer(
        text = 'Отправьте список оплат в формате:\n'
               '(Стоимость) день,день...\n'
               '(Стоимость) день,день...'
    )

@dp.message()
async def process_other_answers(message:Message):
    global PAYMENTS_STATUS

    if PAYMENTS_STATUS == True :
        try:
            result = count_payments(message.text)
            await message.answer(f'Сумма платежей: {result} Руб.')
            PAYMENTS_STATUS = False
        except:
            await message.answer('Ошибка подсчета платежей.\n'
                                 'Убедитесь что данные отправлены в формате:\n'
                                 '(Стоимость) день,день...\n'
                                 '(Стоимость) день,день...' )
    else:
        await message.answer(
            text = 'Выберите команду:',
            reply_markup=start_keyboard
        )






















dp.run_polling(bot)




import asyncio
from time import sleep

from aiogram import Bot,Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton,Message,ReplyKeyboardMarkup,ReplyKeyboardRemove)
from environs import Env


env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#Создаем объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text = 'Огурцов 🥒')

#Создаем объект клавиатуры добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1,button_2]],
                               resize_keyboard=True,
                               one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_command_start(message:Message):
    await message.answer(
        text = 'Чего кошки боятся больше?',
        reply_markup=keyboard
    )

@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message:Message):
    await asyncio.sleep(3)
    await message.answer(
        text = 'Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message:Message):
    await message.answer(
        text = 'Да, иногда кажется, что огурцов '
             'кошки боятся больше',
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message()
async def process_other_answer(message:Message):
    await process_command_start(message)


dp.run_polling(bot)
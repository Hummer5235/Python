#Использование lambda функции в качестве фильтра
from __future__ import annotations

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram import F
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN


# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(lambda message: message.text == '/start')
async def process_start_command(message:Message):
    await message.answer(text='это команда /start')

dp.run_polling(bot)
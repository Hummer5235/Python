
from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton,Message)

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()





kb_builder = ReplyKeyboardBuilder()

buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i+1}') for i in range(15)
]

buttons_2: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i+1}') for i in range(7)
]
#Методами билдера добавляем в него кнопки (возьмем для примера метод row())
# Метод row у класса ReplyKeyboardBuilder позволяет расположить кнопки клавиатуры автоматически,
# в зависимости от параметра width - желаемого количества кнопок в ряду.
# "Лишние" кнопки переносятся на следующий ряд.
kb_builder.row(*buttons_1,width=10)
kb_builder.row(*buttons_2,width=3)



@dp.message(CommandStart())
async def process_command_start(message:Message):
    await message.answer(
        text='Вот такая получается клавиатура',
        reply_markup=kb_builder.as_markup(resize_keyboard = True)
    )



dp.run_polling(bot)


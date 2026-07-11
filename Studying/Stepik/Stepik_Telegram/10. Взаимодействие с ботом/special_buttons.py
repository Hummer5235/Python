
from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType,
                           WebAppInfo)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)

geo_btn = KeyboardButton(
    text='Отправить геопозицию',
    request_location=True
)

poll_btn = KeyboardButton(
    text='Создать опроc/викторину',
    request_poll=KeyboardButtonPollType()
)

vk_app = KeyboardButton(
    text = 'Start Web App',
    web_app=WebAppInfo(url='https://vk.com/wase33')
)

# Добавляем кнопки в билдер
kb_builder.row(contact_btn,geo_btn,poll_btn,vk_app,width=1)

keyboard : ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard = True,
    one_time_keyboard = True
)


@dp.message(CommandStart())
async def process_command_start(message:Message):
    await message.answer(
        text='Экспериментируйте со специальными кнопками',
        reply_markup=keyboard
    )

dp.run_polling(bot)
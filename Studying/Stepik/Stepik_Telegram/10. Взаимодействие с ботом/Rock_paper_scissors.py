from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton,Message,ReplyKeyboardMarkup,ReplyKeyboardRemove)

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import F
from random import choice
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button_1 = KeyboardButton(text='Не хочу!')
button_2 = KeyboardButton(text='Давай!')

game_list_answers = ['Камень','Ножницы','Бумага']

button_rock = KeyboardButton(text = game_list_answers[0])
button_scissors = KeyboardButton(text = game_list_answers[1])
button_paper = KeyboardButton(text = game_list_answers[2])

keyboard_1 = [[button_1,button_2]]
keyboard_2 = [[button_rock,button_scissors,button_paper]]
start_keyboard =  ReplyKeyboardMarkup(
    keyboard= keyboard_1,
    resize_keyboard= True,
    one_time_keyboard=True
)

game_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard_2,
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message(CommandStart())
async def proccess_command_start(message:Message):
    await message.answer(
        text = 'Давай сыграем в камень ножницы бумага?',
        reply_markup = start_keyboard
    )

@dp.message(F.text=='Давай!')
async def proccess_command_start_game(message:Message):
    await message.answer(
        text = 'Отлично! Делай свой выбор!',
        reply_markup = game_keyboard
    )

@dp.message(F.text == 'Камень' )
async def proccess_command_start(message:Message):
    random_answer = choice(game_list_answers)
    await message.answer(
        text = f'Мой ответ: {random_answer}',
        reply_markup = ReplyKeyboardRemove()
    )




dp.run_polling(bot)
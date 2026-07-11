
from aiogram import Bot,Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton,Message,ReplyKeyboardMarkup,ReplyKeyboardRemove)
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Создаем объекты кнопок
button_1 = KeyboardButton(text='Кнопка 1')
button_2 = KeyboardButton(text='Кнопка 2')
button_3 = KeyboardButton(text='Кнопка 3')
button_4 = KeyboardButton(text='Кнопка 4')
button_5 = KeyboardButton(text='Кнопка 5')
button_6 = KeyboardButton(text='Кнопка 6')
button_7 = KeyboardButton(text='Кнопка 7')
button_8 = KeyboardButton(text='Кнопка 8')
button_9 = KeyboardButton(text='Кнопка 9')
button_10 = KeyboardButton(text='Кнопка 10')

#Создаем объект клавиатуры добавляя в него кнопки
# keyboard = ReplyKeyboardMarkup(keyboard=[[button_1,button_2],
#                                          [button_3,button_4],
#                                          [button_5,button_6],
#                                          [button_7,button_8],
#                                          [button_9,button_10]],
#                                resize_keyboard=True,
#                                one_time_keyboard=True)

#Более быстрый способ
# keyboard: list[list[KeyboardButton]] = [[KeyboardButton(text = f'Кнопка {j*3+i}') for i in range(1,4)]for j in range(3)]

#Генерируем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i}') for i in range(1,11)]

# Составляем список списков для будущей клавиатуры
keyboard: list[list[KeyboardButton]] = [
    [buttons[0]],
    buttons[1:3],
    buttons[3:6],
    buttons[6:8],
    [buttons[8]]
]

for el in keyboard:
    for j in el:
        print(isinstance(j,KeyboardButton))
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard= True
)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def proccess_command_start(message:Message):
    await message.answer(
        text = 'Приветствую тебя, выбери цифру',
        reply_markup=my_keyboard
    )



dp.run_polling(bot)
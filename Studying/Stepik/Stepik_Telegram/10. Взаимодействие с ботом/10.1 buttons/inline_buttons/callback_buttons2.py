from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,Message,CallbackQuery
from  environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # П

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

button_1 = InlineKeyboardButton(
    text = 'Тестовая кнопка 1',
    callback_data='button_1'
)

button_2 = InlineKeyboardButton(
    text = 'Тестовая кнопка 2',
    callback_data='button_2'
)

button_3= InlineKeyboardButton(
    text = 'Необычная кнопка 3',
    callback_data='button_3'
)

button_4 = InlineKeyboardButton(
    text='Необычная Кнопка 4',
    callback_data='button_4'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1,button_2],[button_3,button_4]],
)

@dp.message(CommandStart())
async def proccess_command_start(message:Message):
    await message.answer(
        text='Это callback кнопки',
        reply_markup=keyboard
    )

@dp.callback_query(F.data=='button_1')
async def proccess_button_1(callback:CallbackQuery):
    await callback.answer(
        text='Была нажата кнопка 1'
    )

@dp.callback_query(F.data=='button_2')
async def proccess_button_2(callback:CallbackQuery):
    await callback.answer(
        text='Была нажата кнопка 2'
    )

@dp.callback_query(F.data=='button_3')
async def proccess_button_3(callback:CallbackQuery):
    if callback.message.text != 'Была нажата очень необычная кнопка 3, даже поменялось сообщение':
        await callback.message.edit_text(
            text = 'Была нажата очень необычная кнопка 3, даже поменялось сообщение',
            reply_markup=keyboard
        )
    else:
        await callback.answer(
            text='Была нажата очень необычная кнопка 3, сообщение больше меняться не будет'
        )

@dp.callback_query(F.data == 'button_4')
async def proccess_button_4(callback:CallbackQuery):
    await callback.answer(
        text='Была нажата кнопка 4',
        show_alert=True
    )

dp.run_polling(bot)
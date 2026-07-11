from aiogram import Bot, Dispatcher, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,Message,CallbackQuery
from  environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # П

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

kb_builder = InlineKeyboardBuilder()

for index in range(1,11):
    kb_builder.button(text=f'кнопка_{index}',callback_data=f'button_{index}')

kb_builder.adjust(3)

@dp.message(CommandStart())
async def proccess_command_start(message:Message):
    await message.answer(
        text='Это callback кнопки',
        reply_markup=kb_builder.as_markup()
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
            reply_markup=kb_builder.as_markup()
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
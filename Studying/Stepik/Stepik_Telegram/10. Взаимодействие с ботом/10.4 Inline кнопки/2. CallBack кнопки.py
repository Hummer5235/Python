from aiogram.types import CallbackQuery
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок

button_1 = InlineKeyboardButton(
    text='КНОПКА 1',callback_data='button_1_click'
)

button_2 = InlineKeyboardButton(
    text='КНОПКА 2',callback_data='button_2_click'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],[button_2]]
)

@dp.message()
async def process_start(message:Message):
    await message.answer(
        text='Это инлайн кнопки, нажми на любую', reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data `button_1_click`
@dp.callback_query(F.data == 'button_1_click')
async def process_button_1_click(callback: CallbackQuery):
    if callback.message.text != 'Была нажата КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data `button_2_click`
@dp.callback_query(F.data == 'button_2_click')
async def process_button_2_click(callback: CallbackQuery):
    if callback.message.text != "Была нажата КНОПКА 2":
        await callback.message.edit_text(
            text="Была нажата КНОПКА 2",
            reply_markup=callback.message.reply_markup,
        )
    await callback.answer()


dp.run_polling(bot)
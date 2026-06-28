from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env


env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Инициализируем builder
kb_builder = InlineKeyboardBuilder()

#Инициализируем список для кнопок
buttons : list[InlineKeyboardButton] = []

for button_number in range(10):
    buttons.append(
        InlineKeyboardButton(
            text=f'button {button_number}',
            callback_data=f'button {button_number}'
        )
    )

kb_builder.row(*buttons,width=3)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=kb_builder.as_markup()
)

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup = callback.message.reply_markup
        )
    else:
        await callback.answer(text='Ура! Нажата кнопка 1')


dp.run_polling(bot)

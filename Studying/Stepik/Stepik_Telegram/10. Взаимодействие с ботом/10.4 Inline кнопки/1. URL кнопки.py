
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from environs import Env


env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')


LEXICON = {'browser':'Кнопки для перехода в браузер',
           'telegram':'Кнопки для перехода в telegram'}




# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Создаем объекты простых кнопок
browser_selection_button = KeyboardButton(text=LEXICON['browser'])
tg_selection_button = KeyboardButton(text=LEXICON['telegram'])

keyboard_1=[[browser_selection_button,tg_selection_button]]

#Создаем клавиатуру выбора с простыми кнопками
selection_keyboard = ReplyKeyboardMarkup(keyboard=keyboard_1,
                                         resize_keyboard=True)


# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Создатель бота в ВК',url='https://vk.com/wase33'
)

url_button_2 = InlineKeyboardButton(
    text='Кострома на Яндекс картах',url='https://yandex.ru/maps/geo/kostroma/53056941/'
)

url_button_3 = InlineKeyboardButton(
    text='Киржач на Яндекс картах',url='https://yandex.ru/maps/geo/kirzhach/53056876/'
)



# Создаем объекты инлайн-кнопок
channel_name = "zabroskanathach"
url_button_4 = InlineKeyboardButton(
    text='Заброска на Тхач с Адыгеи"', url=f"https://t.me/{channel_name}"
)

user_id = 852757379
url_button_5 = InlineKeyboardButton(
    text="Создатель бота в telegram", url=f"tg://user?id={user_id}"
)

channel_name = "westernwestern"
url_button_6 = InlineKeyboardButton(
    text='Заброска на Тхач с Мостовского',
    url=f"https://t.me/{channel_name}",
)

# Создаем объект инлайн-клавиатуры
browser_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],[url_button_2],[url_button_3]]
)


# Создаем объект инлайн-клавиатуры
telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_4], [url_button_5], [url_button_6]]
)





@dp.message(F.text == LEXICON['browser'])
async def process_browser(message:Message):
    await message.answer(
        text='Это инлайн кнопки с параметром text.\nПереход в браузер', reply_markup = browser_keyboard

    )

@dp.message(F.text == LEXICON['telegram'])
async def process_telegram(message:Message):
    await message.answer(
        text='Это инлайн кнопки с параметром text.\nПереход в телеграмме', reply_markup = telegram_keyboard
    )




@dp.message()
async def process_select(message:Message):
    await message.answer(
        text='Какие кнопки посмотрим?',
        reply_markup = selection_keyboard
    )


dp.run_polling(bot)
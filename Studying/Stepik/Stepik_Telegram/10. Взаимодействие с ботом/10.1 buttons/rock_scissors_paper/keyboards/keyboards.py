from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Создаем кнопки с ответами согласия и отказа
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes,button_no,width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb = yes_no_kb_builder.as_markup(
    one_time_keyboard = True,
    resize_keyboard = True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb =  ReplyKeyboardMarkup(keyboard =
    [[button_rock,
     button_scissors,
     button_paper]],
    resize_keyboard= True
)
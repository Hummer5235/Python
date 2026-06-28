from aiogram.types import (KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

#Кнопки
payments_button = KeyboardButton(text='Посчитать платежи')
guess_date_button = KeyboardButton(text = 'Игра: Угадай дату праздника')
current_date_button = KeyboardButton(text = 'Узнать чем известен сегодняшний день')
back_button = KeyboardButton(text='◀Назад')
exit_game_button = KeyboardButton(text='◀Выйти из игры')

#Кнопки для игры
list_of_numbers = [InlineKeyboardButton(text=f'{index}',callback_data=f'{index}') for index in range(1,32)]
list_of_callback = [str(index) for index in range (1,32)]
yes_button = InlineKeyboardButton(text='Давай',callback_data='yes_button')
no_button = InlineKeyboardButton(text='Не хочу',callback_data='no_button')

# Создаем объекты кнопок
kb_builder = InlineKeyboardBuilder()
kb_builder.add(*list_of_numbers)


#Клавиатура
start_keyboard = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    keyboard = [[payments_button],[guess_date_button],[current_date_button]],
    resize_keyboard=True
)

yes_no_keyboard = InlineKeyboardMarkup(inline_keyboard=[[yes_button,no_button]])

back_keyboard = ReplyKeyboardMarkup(keyboard=[[back_button]],resize_keyboard=True)
exit_game_keyboard = ReplyKeyboardMarkup(keyboard=[[exit_game_button]],resize_keyboard=True)
from aiogram.types import (KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

#Кнопки
payments_button = KeyboardButton(text='\U0001F3E6Посчитать платежи')
guess_date_button = KeyboardButton(text = '\U0001F3AFИгра: Угадай дату праздника')
current_date_button = KeyboardButton(text = '\U0001F4C6Узнать чем известен сегодняшний день')
back_button = KeyboardButton(text='\U000025C0Назад')
exit_game_button = KeyboardButton(text='\U000025C0Выйти из игры')
stats_game_button = KeyboardButton(text='\U0001F4CAПосмотреть статистику')
day_event_mailing_start_button = KeyboardButton(text='\U0001F514Включить оповещения о праздниках')
day_event_mailing_stop_button = KeyboardButton(text='\U0001F515Отключить оповещения о праздниках')
events_button = KeyboardButton(text='\U0001F514Оповещения о праздниках')
get_event_now_button= KeyboardButton(text='\U0001F514Получить оповещение сейчас')

#Дополнительные кнопки админа
admin_button = KeyboardButton(text='\U0001F4BBКоманды админа')
message_for_users_button = KeyboardButton(text='\U0001F4E8Сообщение для пользователей')



#Кнопки для игры
list_of_numbers = [InlineKeyboardButton(text=f'{index}',callback_data=f'{index}') for index in range(1,32)]
list_of_callback = [str(index) for index in range (1,32)]
yes_button = InlineKeyboardButton(text='Давай',callback_data='yes_button')
no_button = InlineKeyboardButton(text='Не хочу',callback_data='no_button')

# Создаем объекты кнопок
kb_builder = InlineKeyboardBuilder()
kb_builder.add(*list_of_numbers)


#Клавиатуры
start_keyboard = ReplyKeyboardMarkup(
    keyboard = [[payments_button],[guess_date_button],[current_date_button],[events_button]],
    resize_keyboard=True
)

start_keyboard_admin = ReplyKeyboardMarkup(
    keyboard = [[payments_button],[guess_date_button],[current_date_button],[events_button],[admin_button]],
    resize_keyboard=True
)

main_keyboard_admin = ReplyKeyboardMarkup(
    keyboard=[[message_for_users_button],[back_button]],
    resize_keyboard=True
)



yes_no_keyboard = InlineKeyboardMarkup(inline_keyboard=[[yes_button,no_button]])
back_keyboard = ReplyKeyboardMarkup(keyboard=[[back_button]],resize_keyboard=True)
exit_game_keyboard = ReplyKeyboardMarkup(keyboard=[[stats_game_button],[exit_game_button]],resize_keyboard=True)

on_events_back_keyboard = ReplyKeyboardMarkup(keyboard=[[day_event_mailing_start_button],[back_button]],resize_keyboard=True)
off_events_back_keyboard = ReplyKeyboardMarkup(keyboard=[[day_event_mailing_stop_button],[get_event_now_button],[back_button]],resize_keyboard=True)
get_event_back_keyboard = ReplyKeyboardMarkup(keyboard=[[get_event_now_button],[back_button]],resize_keyboard=True)


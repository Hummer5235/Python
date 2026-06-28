import telebot
from telebot import types # Для создания кнопок
from Telegram_Token import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


def send_message(message):
    bot.send_message(852757379, message)



# bot.polling(none_stop=True,interval=0)
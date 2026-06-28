import telebot
from Telegram_Token import API_TOKEN
from telebot import types # Для создания кнопок
from User_Data import append_user, read_users
from requests import get
from time import sleep




bot = telebot.TeleBot(API_TOKEN)
API_URL = 'https://api.telegram.org/bot'
users_list = read_users()
users_messages = {i:-1 for i in users_list}
answers = ['Не пишите мне лишние сообщения', 'Эй дружок, я тебя предупреждаю','Еще одно сообщение и ты попадаешь в бан','Готово! Пиши сколько хочешь']
offset = -2

def get_updates():
    global offset
    updates = bot.get_updates(offset=offset+1,timeout=1)
    if updates:
        for result in updates:
            message = result.message
            text = message.text
            chat_id = message.chat.id
            offset = result.update_id
            print(text,chat_id)
            if chat_id not in users_list:
                if text == '/start':
                    bot.send_message(chat_id,'Поздравляю с подпиской! Не пугайся, она бесплатная')
                    users_list.append(chat_id)
                    users_messages[chat_id] = -1
                    append_user(chat_id, users_messages[chat_id])

                else:
                    bot.send_message(chat_id, 'Напишите /start')
            else:
                users_messages[chat_id] += 1
                message_counter = users_messages[chat_id]
                if message_counter <= len(answers) - 1:
                    bot.send_message(chat_id, answers[message_counter])
                else:
                    sleep(0.5)
                    message1 = bot.send_message(chat_id, 'Удаляем)')
                    sleep(0.5)
                    message2 = bot.send_message(chat_id, 'Хаха)')
                    sleep(0.5)
                    bot.delete_message(message.chat.id, message2.message_id)
                    bot.delete_message(message.chat.id, message1.message_id)
                    bot.delete_message(chat_id, message.message_id)

# #


@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users_list:
        if message.text == '/start':
            print(user_id)
            bot.send_message(user_id, 'Поздравляю с подпиской! Не пугайся, она бесплатная')
            users_list.append(user_id)

            users_messages[user_id] = -1
            append_user(user_id,users_messages[user_id])

        else:
            bot.send_message(user_id, 'Напишите /start')
    else:
        users_messages[user_id] += 1
        message_counter = users_messages[user_id]
        if message_counter <= len(answers)-1:
            bot.send_message(user_id, answers[message_counter])
        else:
            bot.delete_message(message.chat.id,message.id)

def send_start_message():
    admin_id = 852757379
    ms = bot.send_message(admin_id, 'Приложение запущено в работу!')


def send_messages(message:str):
    users_list = read_users()
    for user in users_list:
        bot.send_message(user,f'Исторический факт на сегодня: \n{message}')
        print(f'Пользователь с id({user}) № {users_list.index(user)+1}  из {len(users_list)} оповещен')

def error_notification():
    bot.send_message(852757379, 'Пожалуйста проверьте приложение!')


# bot.polling(non_stop=True,interval=0)
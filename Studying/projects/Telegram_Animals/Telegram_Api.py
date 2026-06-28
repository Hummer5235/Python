import telebot
import time
import requests
from Telegram_Token import API_TOKEN
from Cats_Api import API_CATS_URL



bot = telebot.TeleBot(API_TOKEN)
API_URL = 'https://api.telegram.org/bot'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
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
            for i in range(5):
                res = requests.get(API_CATS_URL)
                if res.ok:
                    link = res.json()[0]['url']
                    bot.send_photo(chat_id, photo=link)
                else:
                    bot.send_message(chat_id,ERROR_TEXT)

    return True

from requests import get
import time
from environs import Env

API_URL = 'https://api.telegram.org/bot'

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN')

offset = -2
timeout = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['chat']['id']
            print(chat_id)
            do_something()
            get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=...')

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
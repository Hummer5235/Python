from requests import get
from time import sleep
from random import choice
from environs import Env

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
API_FOX_URL = 'https://randomfox.ca/floof/'

API_URLS = (API_CATS_URL,API_DOGS_URL,API_FOX_URL)

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN')

TEXT = 'Ура, классный апдейт!'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER = 100


offset = -2
counter = 0



while counter < MAX_COUNTER :
    print('attempt =',counter)
    updates = get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            random_api = choice(API_URLS)
            photo_response = get(f'{random_api}')

            if photo_response.status_code == 200:
                if random_api == API_CATS_URL:
                    print(photo_response.json())
                    photo_link = photo_response.json()[0]['url']
                elif random_api == API_DOGS_URL:
                    print(photo_response.json())
                    photo_link = photo_response.json()['url']
                else:
                    print(photo_response.json())
                    photo_link = photo_response.json()['link']

                get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={photo_link}')

            else:
                get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

            # get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    sleep(1)
    counter+=1

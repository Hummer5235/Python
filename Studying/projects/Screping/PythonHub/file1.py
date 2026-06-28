import time
import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep



ua = UserAgent()

url = 'https://gtrk-kostroma.ru/'

headers = { "User-Agent": ua.random, "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.7", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}




counter = 0
false_answer = 0

all_news_data = []  # Список для хранения всех новостей



def save_news_to_json(news_item,filename= 'news_data.json'):
    try:
        # Пытаемся прочитать существующие данные
        with open(filename,'r',encoding='utf-8') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        # Если файла нет или он невалидный, создаём пустой список
        existing_data = []

    # Перезаписываем файл целиком
    existing_data.append(news_item)

    # Перезаписываем файл целиком
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(existing_data,f,ensure_ascii=False,indent=4)
        print("Файл news_data.json успешно обновлен.",end='\n\n\n')




for page_number in range(1,100):

    url_with_pages = f'{url}?PAGEN_2={page_number}'

    time.sleep(10)

    responce = requests.get(url_with_pages, headers=headers)

    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find_all('div', class_="news news--lenta")



    if data:
        for i in data:


            news_link = i.find('a').get('href')



            news_date = i.find('span',class_='news__date').text.strip().capitalize()
            name = i.find('span',class_='news__name').text.strip()
            news_text = i.find('span',class_='news__text').text.strip()
            url_img = i.find('img').get('src')

            counter += 1

            print(counter)
            print('news_date:', news_date)
            print('name:', name)
            print('news_link', url + news_link)
            print('news_text:', news_text)
            print('url_img', url + url_img)

            news_item = {
                'news_id':counter,
                'news_date': news_date,
                'name': name,
                'news_link': url + news_link,
                'news_text': news_text,
                'url_img': url + url_img,
            }

            save_news_to_json(news_item)

            # all_news_data.append(user_data)  # Добавляем новость в общий список
    else:
        false_answer += 1

    if false_answer == 5:
        print('False answers')
        break



# with open("user_profile.json", "w", encoding="utf-8") as f:
#     json.dump(all_news_data, f, indent=4, ensure_ascii=False, sort_keys=False)



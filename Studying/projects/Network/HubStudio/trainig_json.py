#Тренируемся с парсингом json файла

import requests , googletrans
from googletrans import Translator
import time

translator = Translator()
result = translator.translate('text', dest='ru')






def get_posts(trans = False):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    js = response.json()
    start_time = time.time()
    with open('txt_files/posts.txt', 'w', encoding='utf-8') as out:
         for post in js:
            if trans:
                id, body = post['id'],translator.translate(post['body'],dest='ru').text
            else:
                id, body = post['id'],post['body']
            out.write(f'{id}\n{body}\n\n')
            print(id,body)

    working_time = round(time.time() - start_time,2)
    print(working_time)

def get_comments(trans=False):
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    js = response.json()
    start_time = time.time()
    with open('txt_files/comments.txt', 'w', encoding='utf-8') as out:
        for comment in js:
            if trans:
                id, body = comment['id'],translator.translate(comment['body'], dest='ru').text
            else:
                id,body = comment['id'],comment['body']
            out.write(f'{id}\n{body}\n\n')
            print(id, body)

    working_time = round(time.time() - start_time, 2)
    print(working_time)

def get_photo():
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    js = response.json()
    start_time = time.time()
    with open('txt_files/photos.txt', 'w', encoding='utf-8') as out:
        for photo in js:
            id, url = photo['id'], photo['url']
            out.write(f'{id}\n{url}\n\n')
            print(id, url, sep='\n')

        working_time = round(time.time() - start_time, 2)
        print(working_time)

get_posts(True)
get_comments(True)
get_photo()
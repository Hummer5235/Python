
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
           }
response = requests.get('https://www.kinoafisha.info/rating/movies/',headers=headers)
soup  = BeautifulSoup(response.text,'html5lib')
films = soup.find_all('div',class_ = 'movieItem_info')
rates_list=list(map(lambda x: x.text, soup.find_all('span',class_='movieItem_itemRating miniRating miniRating-good')))

data = []

for film_tuple in enumerate(films):
    number,film_info = film_tuple
    film = film_info.find('a',class_='movieItem_title')
    link = film.get('href')
    film_type = film_info.find('div',class_='movieItem_details').find('span',class_='movieItem_genres').text
    russian_name = film.text
    rate = rates_list[number].replace('.',',')
    if [russian_name,film_type,rate,link] not in data:
        data.append([russian_name,film_type,rate,link])
    print(f'''{number+1}.Название: {russian_name}, Оценка: {rate}
Жанр: {film_type}
Ссылка: {link}''',end='\n\n')

header = ['russian_name','film_type','rate','link']
df = pd.DataFrame(data,columns=header)
df.to_csv(r'C:\Users\PC\Desktop\kinoafisha_data.csv',sep=';',index=False,encoding='cp1251')



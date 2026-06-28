import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
           }


response = requests.get('https://www.aviasales.ru/search/MOW1101LED1',headers=headers).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div',class_='web-app') #Ищем одно совпадение
print(block)
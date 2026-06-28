import requests
from bs4 import BeautifulSoup

# response = requests.get('https://icanhazip.com/')


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
           }

response = requests.get('https://browser-info.ru/',headers=headers).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div',id='tool_padding') #Ищем одно совпадение

#Check js
check_js = block.find('div',id='javascript_check')
result_js = check_js.find_all('span')[1]
# print('JavaScript',result_js.text)


#Check flash
check_flash = block.find('div',id='flash_version')
result_flash = check_flash.find_all('span')[1]
# print('Flash',result_flash.text)
# print(response.text)
# print(response.status_code)


#Check user-agent
check_user = block.find('div',id = 'user_agent')
# print('User-agent',check_user)

# with open('1.html','w',encoding='utf-8') as file:
#     file.write(response.text)


# response = requests.get('https://www.aviasales.ru/search/MOW1101LED1',headers=headers).text
# soup = BeautifulSoup(response,'lxml')
# block = soup.find('body').find('div',class_='header').find('div',class_='web-app') #Ищем одно совпадение
# print(block)


# response = requests.get('https://grandtrain.ru/tickets/2000000-2004000/15.01.2024/054Ч/',headers=headers)
# soup= BeautifulSoup(response.text,'lxml')
# block = soup.find_all('span',class_='car-class__fare-mb-seats')
# print(*block,sep='\n')
# for i in block:
    # el = i.find_all('span')[0]
    # print(soup.select_one('span',el))


# print(*block,sep='\n')

# for carriage in block:
#     print(*[str(x).replace('<span>','') for x in carriage.find_all('span')])


resonse = requests.get('https://www.kinopoisk.ru/lists/movies/top250/',headers=headers)

soup = BeautifulSoup(resonse.text,'lxml')
print(soup.prettify())

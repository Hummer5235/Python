import requests , webbrowser
from apikey import APITOKEN
inp = input('Введите запрос для поиска: ')

params = {'q':inp,'appid':APITOKEN,'units':'metric','lang':'ru'}

response = requests.get('https://api.openweathermap.org/data/2.5/weather',params= params)


print(response.json())
print(response.headers)

# with open('page.html', 'w', encoding='utf-8') as out:
#     out.write(response.text)
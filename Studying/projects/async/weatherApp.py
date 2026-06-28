import requests
import time

#Обычная версия программы погоды. Последовательное выполнение

def get_weather(city):

        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q':city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        response = requests.get(url=url,params=params)
        weather_json = response.json()
        print(f'{city}: {weather_json["weather.py"][0]["main"]}')


def main():
    for city in cities:
        get_weather(city)



cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


print(time.strftime('%X'))
main()
print(time.strftime('%X'))
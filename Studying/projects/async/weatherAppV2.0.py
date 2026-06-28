import asyncio
import time
from aiohttp import ClientSession

# Асинхронная версия погоды


async def get_weather(city):
    async with ClientSession() as session:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q':city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url,params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather.py"][0]["main"]}')


async def main():
    tasks = []
    for city in cities:
        task = asyncio.create_task(get_weather(city))
        tasks.append(task)

    for task in tasks:
        await task

    #Групповой запуск задач
    results = await asyncio.gather(*tasks)
    # for result in results:
    #     print(result)




cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


print(time.strftime('%X'))
asyncio.run(main())
print(time.strftime('%X'))
from weather_api_service import Weather, Temperature_scale, WeatherType
from datetime import datetime

def format_weather(weather: Weather) -> str:
    '''Здесь будет печать данных погоды из структуры weather'''

    return (f'{weather.city}: {weather.weather_type}\n'
            f'Температура: {weather.temperature}{Temperature_scale}\n'
            f'Восход: {weather.sunrise}\n'
            f'Закат: {weather.sunset}')


if __name__ == '__main__':
    print(format_weather(Weather(temperature= 25,
                   weather_type= 'Солнечно',
                   sunrise = datetime.fromisoformat('2023-12-08 09:22:00'),
                   sunset = datetime.fromisoformat('2023-12-08 16:22:00'),
                   city='Москва'
    )))


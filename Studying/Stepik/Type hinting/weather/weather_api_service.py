from enum import Enum
from exceptions import ApiServiceError
from datetime import datetime
from typing import NamedTuple
import requests
from apikey import APITOKEN

from coordinates import Coordinates

Celsius = int
Temperature_scale = '°C'

class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    FOG = 'Туман'
    CLOUDS = 'Облачно'
    RAIN = 'Дождь'


class Weather(NamedTuple):
    temperature : Celsius
    weather_type : WeatherType
    sunrise : datetime
    sunset : datetime
    city : str


def get_weather(coordinates : Coordinates)-> Weather :
    response = _get_weather_response(coordinates)
    weather = _parse_weather_response(response)
    return weather


def _get_weather_response(coordinates):
    lat, lon = coordinates
    params = {'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'appid': APITOKEN}
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?', params=params)
        if response.status_code != 200:
            raise ApiServiceError
    except :
        raise ApiServiceError

    return response

def _parse_weather_response(response):
    result = response.json()
    # print(result)
    temperature = round(result['main']['temp'],1)
    weather_type = result['weather'][0]['description'].capitalize()
    sunrise = datetime.fromtimestamp(result['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(result['sys']['sunset']).strftime('%H:%M')
    city = result['name']
    return Weather(temperature= temperature,
                   weather_type=weather_type,
                   sunrise = sunrise,
                   sunset = sunset,
                   city=city
                   )

if __name__ == '__main__':
    get_weather(Coordinates(10,20))
#!C:\Users\zahar\AppData\Local\Programs\Python\Python39\python.exe

from ip import get_ip
from exceptions import CantGetCoordinates, ApiServiceError
from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather

def main():
    ip = get_ip('https://api64.ipify.org?')
    try:
        coordinates = get_coordinates(ip)
    except CantGetCoordinates:
        print('Не удалось получить GPS координаты')
        exit(1)

    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f'Не удалось получить погоду по координатам {coordinates}')
        exit(1)
    print(format_weather(weather))

if __name__ == '__main__':
    main()

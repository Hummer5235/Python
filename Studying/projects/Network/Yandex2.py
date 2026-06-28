import requests
from requests import get, ReadTimeout, ConnectionError,ConnectTimeout,HTTPError,Timeout
import webbrowser

params = {"ll": "40.927779,57.768846",
          "spn": "0.016457,0.00619",
          "l": "map"}

try:
    response = get("https://static-maps.yandex.ru/1.x/?",params=params,timeout=30)
    print(response.status_code)

except requests.ConnectionError:
    print('Проверьте подключение к сети или адрес сайта')
except HTTPError :
    print('Неверный адрес')
else:
    with open('map.png', 'wb') as file:
        file.write(response.content)
    pass






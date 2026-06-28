import requests
from apikey import APITOKEN
from test2 import lat, lon

params = {'lat':lat,'lon':lon,'appid':APITOKEN}
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?',params=params)
print(response.json())


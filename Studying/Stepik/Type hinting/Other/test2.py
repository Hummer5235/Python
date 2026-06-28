import requests
from geopy.geocoders import Nominatim


#Получение ip
responce = requests.get('https://api64.ipify.org?format=json').json()
ip = responce['ip']

params = {'ip':ip}

#Получение города
responce2 = requests.get('https://ipapi.com/ip_api.php?',params=params)
city = responce2.json()['city']
print(city)
#
# app = Nominatim(user_agent='tutorial')
#
# responce = app.geocode(city).raw
# lat,lon  = responce['lat'], responce['lon']
# print(lat,lon)

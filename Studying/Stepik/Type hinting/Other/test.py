# import requests
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36",
# }
#
#
# responce = requests.get('https://geotree.ru/geolocation')
# print(responce.text)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_user_agent")
city ="Gorohovets"
country ="Uk"
loc = geolocator.geocode(city)
print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
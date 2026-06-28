from geopy.geocoders import Nominatim

geo = Nominatim(user_agent="Tester")
addr= input('Введите адрес: \n')
location = geo.geocode(addr)

print(location.latitude,location.longitude)
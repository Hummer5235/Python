from geopy.geocoders import Nominatim

def get_location(city):
    geo = Nominatim(user_agent="Tester")
    addr = city
    location = geo.geocode(addr)
    return location

if __name__ == '__main__':
   get_location()

from exceptions import CantGetCoordinates , ApiServiceError
from typing import NamedTuple , Literal , Union
import ipinfo
from config import  USE_ROUNDED_COORDS

access_token = '1e3fc018849400'
handler = ipinfo.getHandler(access_token)


"""Именованные кортежи — такие же кортежи, как и обычные tuple, 
но каждый элемент кортежа имеет имя, по которому мы можем к нему обращаться"""

class Coordinates(NamedTuple):
    latitude : float
    longitude : float


def get_coordinates(ip: str) -> Coordinates: #Указываем что будет возвращаться
    """Returns current GPS coordinates using special service"""
    try:
        details = handler.getDetails(ip)
    except ValueError:
        raise CantGetCoordinates
    lat,lon = map(float,details.loc.split(','))

    if USE_ROUNDED_COORDS :
        lat,lon = map(lambda x: round(x,1),(lat,lon))
    return Coordinates(lat,lon)














coordinates = get_coordinates('188.112.133.21')
print(coordinates)
# print(coordinates.latitude)
# print(coordinates.longitude)





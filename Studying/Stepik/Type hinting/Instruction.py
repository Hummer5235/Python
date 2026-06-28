#Type hinting - аннотация типов
from typing import Literal, Union , NamedTuple
from dataclasses import dataclass

#Тип определенной переменной
name : str
age : Union[int,float]

#тип всех элементов списка
a: list[int]
a2: list[int]

#тип каждого элемента кортежа
b: tuple[int,float]

#тип ключей, тип значений
c: dict[str,float]

#тип всех элементов множества
valid_answers: set[str]

a = ['12',12,3,4]
a2 = ['12']
b = (12,12)

def say_name(name:str):
    print(f'Привет, мое имя:{name}')


say_name('Alex')


#Указываем что будет возвращаться
#Только одно из двух значений, конкретное
def get_gps_coordinates() -> Union[Literal['latitude'] , Literal['longitude']]  :
    return 'longitude'

#Именованный кортеж
class Coordinates(NamedTuple):
    latitude : float
    longitude : float

#Датакласс
@dataclass
class Coordinates2():
    latitude : float
    longitude : float

coord1 = Coordinates(10,20)
coord2 = Coordinates2(10,20)
print(coord1,coord2,sep = '\n')
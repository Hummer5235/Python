#Инициализатор и финализатор
# __init__(self) вызывается сразу после создания объекта класса
# __del__(self)  автоматически вызывается непосредственно перед уничтожением экземпляра класса
import time
import pygame


class Point():
    'Класс для представления координат точек на плоскости'
    color = 'red'
    circle = 2
    
    def __init__(self, x=0, y=0):
        print("Вызов метода __init__")
        self.x = x
        self.y = y
        
    def __del__(self):
        print(f"Удаление экземпляра {self}")
    
pt1 = Point(1,2)
pt2 = Point()
print(pt1.__dict__)
print(pt2.__dict__)

t = 5
for i in range(t):
    time.sleep(1)
    print(f'Время до удаления экземпляров: {4-i}')



    



        
    

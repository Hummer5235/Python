
# Использования модуля accessify для защиты от изменений

from accessify import private, protected


class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
    
    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)
    
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y) :
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
        
    def get_coord(self):
        return self.__x, self.__y
        
pt = Point(1, 't')
# pt.set_coord(10, 2.3)
print(pt.get_coord())
print(dir(pt))
print(pt._Point__x) # Обращение к приватному свойству класса
print(pt._Point__check_value(5)) # Обращение к приватному методу класса



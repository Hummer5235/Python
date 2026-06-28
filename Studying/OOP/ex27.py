#27. Как работает __slots__ с property и при наследовании
'''
Пока в этом классе нет коллекции __slots__, поэтому при создании его экземпляра можно свободно оперировать
существующими свойствами.
Как известно, список всех локальных свойств экземпляра класса хранится в его магическом списке __dict__

'''

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x**2 + y**2) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

pt1 = Point2D(10, 20)
print(pt1.length)
pt1.length = 5
print(pt1.length)

'''
Не смотря на наличие коллекции __slots__ мы можем использовать методы с 
'''
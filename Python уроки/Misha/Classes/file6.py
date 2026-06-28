#classmethod и staticmethod
#Методы класса и статические методы


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self,x,y):
        if Point.check(x) and Point.check(y):
            self.x = x
            self.y = y
        else:
            self.x = self.y = 0

    def get_coords(self):
        return self.x,self.y

    # @classmethod #Декоратор для метода класса
    def check(cls,arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def quare(x,y):
        return x**2 + y**2



#Вариант1
p = Point(10,20)
coord = p.get_coords()
print(coord)

#Вариант2
p = Point(10,102)
coord = Point.get_coords(p) #Вызываем метод у класса и передаем объект
print(coord)

res = Point.check(10)
print(res)

Point.check(50)

#Классы
#Класс - шаблон кода (набор инструкций) для создания объектов
#ООП (объектно ориентированное программирование) - подход для моделирования вещей, отношений между ними
#Атрибут - свойство объекта. Характеристика
#Метод - функция, привязанная к типу данных
# self - ссылается, на только что созданный экземпляр

car = ['Зеленый','Mersedes','Универсал']


class Car:
    def __init__(self,color,brand, speed): #Конструктор - с него начинается создание объектов
        self.color = color
        self.brand = brand
        self.distance = 0
        self.speed = speed

    def __str__(self):
        return f'Car({self.color},{self.brand}); Distance = {self.distance}'

    def update(self):
        self.distance += self.speed




mers = Car('Красный','Mersedes',200)
bmw = Car('Синий','BMW',150)
print(mers)
print(bmw)

mers.update()
bmw.update()
bmw.update()
mers.update()
bmw.update()

print(mers)
print(bmw)


# print(mers.color)
# print(mers.brand)




# print(bmw.color)
# print(bmw.brand)


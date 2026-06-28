#Методы - функции, привязанные к типу данных

class Point:
    '''My class for points'''
    color = 'blue' #Переменные внутри класса - атрибуты, свойства
    circle_rad = 5

    def set_coords(self,x,y):
        self.x = x
        self.y = y
        print('Вызов метода set_coords')

    def get_coords(self):
        print(self.x,self.y)

a = Point()
a.set_coords(1,2)

b = Point()
b.set_coords(3,4)

a.get_coords()
b.get_coords()



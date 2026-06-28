#Магический метод :   __имя метода__
#Инициализатор __init__ - вызывается сразу после создания объекта, используется для создания свойств(атрибутов) объекта

class Point:
    '''My class for points'''
    color = 'blue' #Переменные внутри класса - атрибуты, свойства
    circle_rad = 5

    def __init__(self,x,y):
        print('вызов __init__')
        self.x = x
        self.y = y

    def set_coords(self,x,y):
        self.x = x
        self.y = y
        print('Вызов метода set_coords')

    def get_coords(self):
        print(self.x,self.y)

point1 = Point(15,15)
point1.get_coords()





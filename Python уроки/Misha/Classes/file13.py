class Geom:
    name = 'Geom'
    def __init__(self,x1,x2):
        print(f'Инициализатор Geom для {self.__class__}')
        self.x1 = x1
        self.x2 = x2
    # def __init__(self):
    #     print('Инициализатор Geom')

    def draw(self):
        print("Рисование объекта")

class Line(Geom):

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self,x1,x2,fill = None):
        print('Инициализатор Rect')
        # Geom.__init__(self,x1,x2) # Запустить инициализатор в базовом классе
        super().__init__(x1,x2) # Возвращает ссылку на базовый класс
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")
        print(self.x1,self.x2)


line1 = Line(0,10)
line1.draw()

rect = Rect(10,20,True)
rect.draw()
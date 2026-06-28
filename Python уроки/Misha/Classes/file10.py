#Наследование - Один класс наследует атрибуты и методы другого

class Geom:
    name = 'Geom'

 
 
class Line(Geom):
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
    def draw(self):
        print("Рисование линии")



class Rect(Geom):
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
    def draw(self):
        print("Рисование прямоугольника")

g = Geom()
print(g.name)

l = Line()
l.draw()

r = Rect()
l.set_coords(0,0,10,10)
r.set_coords(2,2,12,12)


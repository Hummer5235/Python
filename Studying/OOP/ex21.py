#21. Функция issubclass(). Наследование от встроенных типов и от object
#Пользовательский класс наследуется от базового класса object
#Все стандартные типы данных являются классами. Все наследованы от object

class Geom:
    pass


class Line(Geom):
    pass

g = Geom()
l = Line()
print(issubclass(Line, Geom))
print(issubclass(l.__class__, Geom))
print(isinstance(l, Geom))
print(isinstance(int, object))

#Полиморфизм - возможость работы с совершенно разными объектами (Языка Python) единым образом

'''
Абстрактные методы - это методы, которые обязательно нужно переопределять в дочерних классах и которые
не имеют своей собственной реализации
Конечно, в языке Python нет чисто абстрактных методов. Здесь мы лишь выполнили имитацию их поведения,
заставляя программиста определять геттер get_pr() в дочерних классах, самостоятельно генерируя
исключение NotImplementedError.
'''

# Мы называем методы одинаковым именем , для дальнейшего ипользования в  универсальном коде программы

class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)

class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(5,6,7)
t2 = Triangle(10,12,13)

geom = [r1, r2, s1, s2, t1, t2]
for g in geom:
    print(g.get_pr())

# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())


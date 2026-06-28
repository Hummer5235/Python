#Полиморфизм – это возможность работы с совершенно разными объектами (языка Python) единым образом.

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
 
    def get_pr(self):
        return 2*(self.w+self.h)
 
class Triangle:
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a+self.b+self.c

 
class Square:
    def __init__(self, a):
        self.a = a
 
    def get_pr(self):
        return 4*self.a


r1 = Rectangle(5,7)
r2 = Rectangle(13,4)



s1 = Square(8)
s2 = Square(14)





figures = [r1,r2,s1,s2]

for fig in figures:
	print(fig.get_pr(),'m2')

# for fig in figures:
# 	if isinstance(fig,Rectangle):
# 		print(fig.get_rect_pr())
# 	else:
# 		print(fig.get_sq_pr())


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for i in geom:
	print(i.get_pr(),'sm2')
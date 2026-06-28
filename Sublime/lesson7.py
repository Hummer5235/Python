import math

#Создание класса и его методов

class Point:
	list_point = []

	#Магический метод инициализация
	def __init__(self, coord_x = 0, coord_y=0):
		self.move_to(coord_x,coord_y)
		Point.list_point.append(self)

	#Метод назначения новых координат точке
	def move_to(self,new_x,new_y):
		self.x = new_x
		self.y = new_y

	#Метод возвращения в координаты 0,0
	def go_home(self):
		self.move_to(0,0)

	#Метод распечатывания координат точки
	def print_point(self):
		print(f"Точка с координатами ({self.x},{self.y})")


	# Расстояние между точками (по теореме Пифагора)
	def calc_distance(self,another_point):
		#Функция isinstance( ) проверяет является ли аргумент объект экземпляром класса 
		#или экземпляром класса из кортежа
		if not isinstance(another_point,Point):
			raise ValueError("Аргумент должен принадлежать классу Точка")

		return math.sqrt((self.x-another_point.x)**2 + (self.y-another_point.y)**2)



a = Point()
print(a.x,a.y)
a.move_to(0,0)
a.print_point()
b = Point(4,3)
c = 15
print(a.calc_distance(b))

print(Point.list_point[1].x,Point.list_point[1].y)

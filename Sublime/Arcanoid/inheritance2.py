class Transport():
	def __init__(self,name,speed,carrying):
		self.name = name
		self.speed = speed
		self.carrying = carrying


t1 = Transport("Car",220,1500)
print(t1)
print(t1.name)
print(t1.speed)
print(t1.carrying)


class car(Transport):
	def __init__ (self,name,speed,carrying,brand,color,doors):
		Transport.__init__(self,name,speed,carrying)
		self.brand = brand
		self.color = color
		self.doors = doors

c1 = car("Car",220,2000,"BMW","red",5)
print(c1)
print(c1.brand)
print(c1.color)
print(c1.doors)


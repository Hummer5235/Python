class Car:
	def __init__(self,color,brand,speed):
		self.color = color
		self.brand = brand
		self.distance = 0
		self.speed = speed
	def __str__(self):
		return f"Car({self.color},{self.brand}); Distance = {self.distance}"

	def update(self):
		self.distance +=self.speed


mersedes = Car("red","mersedes",10)
bmw = Car("green","bmw",12)

bmw.update()
mersedes.update()
mersedes.update()
print(mersedes)
print(bmw)

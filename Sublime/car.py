#Класс Car
class Car:
	def __init__ (self,color,brand,speed):
		self.color = color
		self.brand = brand
		self.speed = speed
		self.distance = 0

	def __str__ (self):
		return f"Car({self.color},{self.brand}),Distance={self.distance}"

	def update(self):
		self.distance += self.speed

mersedes = Car("red","mersedes",10)
bmw = Car("blue","bmw",8)


mersedes.update()
bmw.update()
bmw.update()
mersedes.update()

print(mersedes)
print(bmw)


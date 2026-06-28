class Cat:
	breed = "pers"

	def __init__(self,name,breed = "pers",age = 1,color = "white"):
		self.name = name 
		self.breed = breed
		self.age = age
		self.color = color

a = Cat("walt",age=13)
print(a.name,a.breed,a.age,a.color)


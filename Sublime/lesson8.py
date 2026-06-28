# Моносостояние
# Изменение атрибутов одного экземпляра влияет на все ост экземпляры
# Т.к. словатрь - изменяемый объект 

class Cat:
	__shared__attr={
		"breed":"pers",
		"color":"black"
	}

	def __init__(self):
		self.__dict__ = Cat.__shared__attr

a = Cat()
b = Cat()

a.color = "white"
print(a.color)
print(b.color)

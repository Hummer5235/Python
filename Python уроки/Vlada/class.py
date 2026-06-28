#Класс - тип данных, описывающий устройство объектов
#Объект - это экземпляр класса.
#Атрибуты - свойства
#Методы - действия

class Parrot:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	#Метод экземпляра
	def sing(self, song):
		return f"Поет : {song}"

		


blue = Parrot("Блу",7)
print(blue.name,blue.age)

orange = Parrot("Оранж",12)
print(orange.name,orange.age)

print(blue.sing("Ура,ура!!!"))
print(orange.sing("Я оранжевый попугай!"))



# Наследование классов
"""Создание нового класса на основе существующего"""

class Person():
	def __init__(self,name):
		self.name = name

	def say_name(self):
		print(f"Hello! I am {self.name}")


class Student(Person): # От какого класса наследовать
	def __init__(self,name,age): # Указываем параметры Род класса и новые по желанию
		Person.__init__(self,name) # Вызов метода __init__ класса Person для инициализации
		self.age = age # Создание атрибута age для класса Student

	def get_years(self):
		print(f"{self.name} is {self.age} years old")

person1 = Person("Petr")
person1.say_name()

s = Student("Ivan", 23)
s.say_name()
s.get_years()

s2 = Student("Misha",120)
s3= Student("Seva",90)

s2.get_years()
s3.get_years()
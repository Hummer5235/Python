#Наследование классов
"""Создание нового класса на основе существующего. При необходимости перезаписываем 
или перегружаем методы или некоторые атрибуты."""

class Person():
	def __init__(self,name):
		self.name = name
	def say_name(self):
		print(f"Hello! I am {self.name}")

#Наследование - создание еще одного класса с тем же набором свойств,атрибутов, методом которые мы создали .


class Student(Person):
	def __init__(self,name,age):
		Person.__init__(self,name)
		self.age = age
	def get_years(self):
		print(f'{self.name} is {self.age} years old')

p = Person("Petr")
p.say_name()


s = Student("Ivan",23)
s.say_name()
s.get_years()

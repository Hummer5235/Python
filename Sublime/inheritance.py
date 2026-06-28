# Наследование - создание еще одного класса с тем же набором свойств, атрибутов, методов.
# При необходимости перегружаем методы или атрибуты 

class Person:
	def __init__(self,name):
		self.name = name
	def say_name(self):
		print(f"Hello! I am {self.name}")		

class Student(Person):
	def __init__(self,name,age):
		Person.__init__(self,name)
		self.age = age


p = Person("Ivan")
p.say_name()

s = Student("Alex",20)
s.say_name()
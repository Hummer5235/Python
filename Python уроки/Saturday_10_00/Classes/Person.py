#Наследование

class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'Hello! I am {self.name}')



class Student(Person):
    def __init__(self,name,age):
        Person.__init__(self,name) #Запуск класса Person
        self.age = age

    def get_age(self):
        print(f'{self.name} is {self.age} years old')



s1 = Student('Ivan',5)
s1.say_name()
s1.get_age()

s1 = Student('Andrey',2)
s1.get_age()






per1 = Person('Kirill')
per1.say_name()

per2 = Person('Zahar')
per2.say_name()

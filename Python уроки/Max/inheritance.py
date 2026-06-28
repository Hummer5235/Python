class Person:
    def __init__(self,name):
        self.name = name

    def say_name(self):
        print(f"Hello, my name is {self.name}")




class Student(Person):
    def __init__(self,name,age,eyes_color):
        Person.__init__(self,name)
        self.age = age
        self.eyes_color = eyes_color

    def get_years(self):
        print(f"{self.name} is {self.age} years old, my eyes are {self.eyes_color}")



p = Person("Max")
s = Student("Jon",21,"blue")

p.say_name()
s.get_years()
s.say_name()
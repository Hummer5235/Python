#13. Магические методы __str__, __repr__, __len__, __abs__

'''
__str__() – магический метод для отображения информации об объекте класса для пользователей
(например, для функций print, str);

__repr__() – магический метод для отображения информации об объекте класса в режиме отладки
(для разработчиков).
'''

class Cat:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'{self.__class__} : {self.name}'
    
    def __str__(self):
        return f'{self.name}'
        
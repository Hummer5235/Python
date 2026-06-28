#7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__
#Атрибуты класса являются общими для всех экземпляров класса

"""
__setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса;

__getattribute__(self, item) - автоматичкески вызывается при получении свойства класса с именем item;

__getattr__(self, item) - автоматичкески вызывается при получении несуществующего свойства item класса;

__delattr__(self, item) - автоматичкески вызывается при удалении свойства item (не важно сущ оно или нет);
"""
class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    #Магический метод получения атрибута
    def __getattribute__(self, item):
        print('вызов __getattribute__')
        
        #Сделали ограничение на получение свойства x
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)
    
    #Магический метод создания атрибута
    def __setattr__(self, key, value):
        print("вызов __setattr__")
        if str.lower(key) == 'z':
            raise ValueError('Недопустимое имя атрибута')
        else:
            return object.__setattr__(self, key, value)
    
    #Магический метод обработка несущесвующего атрибута
    def __getattr__(self, item):
        print('вызов __getattr__')
        print('такого атрибута нет')
        return False

    # Магический метод удаления атрибута
    def __delattr__(self, item):
        print('вызов __delattr__')
        object.__delattr__(self, item)

    
    
pt = Point(1,2)
# print(pt.x)
print(pt.y)
print(pt.z)
del pt.y
print(pt.__dict__)

#Для изменения атрибута класса

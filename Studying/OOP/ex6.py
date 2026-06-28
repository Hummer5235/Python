#6. Режимы доступа public, private, protected. Сеттеры и геттеры
#Механизм инккапсуляции
#Ограничение доступа к данным и методам класса извне
'''Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным). Инкапсуляция делает
некоторые из компонент доступными только внутри класса. Инкапсуляция в Python работает лишь на уровне соглашения
между программистами о том, какие атрибуты являются общедоступными, а какие — внутренними.'''


'''
atribute (без одного или двух подчеркиваний вначале) - публичное
свойство - public

_attribute (с одним подчеркиванием) - режим доступа protected
служит для обращения внутри класса и во всех его дочерних классах - не ограничивает доступ извне, только
предостерегает к использованию

__attribute (с двумя подчеркиваниями) - режим доступа private
(служит для обращения только внутри класса)
'''

#Доступ private
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
            
    @classmethod
    #Приватный метод класса
    def __check_value(cls, x):
        return type(x) in (int, float)
    
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y) :
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
        
    def get_coord(self):
        return self.__x, self.__y
        
pt = Point(1, 't')
# pt.set_coord(10, 2.3)
print(pt.get_coord())


print(dir(pt))
print(pt._Point__x) # Обращение к приватному свойству класса
print(pt._Point__check_value(5)) # Обращение к приватному методу класса




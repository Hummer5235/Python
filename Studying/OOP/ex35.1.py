#35. Пользовательские метаклассы. Параметр metaclass
#Создание метакласса ввиде класса

'''
инициализатор __init__() в классе Meta вызывается когда класс Point полностью создан.
Для более тонкой работы лучше переопределить магический метод __new__, который вызывается
непосредственно перед созданием класса. В нашем случае это можно сделать так:
'''
'''
Так как метод __new__ вызывается до создания нового класса, то мы добавляем новые атрибуты
MAX_COORD и MIN_COORD непосредственно в словарь attrs. А, затем, вызываем аналогичный 
метод __new__ у объекта-метакласса type. Обратите внимание, метод __new__ должен вернуть 
ссылку на созданный класс, то есть, обязательно следует прописать оператор return.
'''
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD' : 100, 'MIN_COORD' : 0})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())

#35. Пользовательские метаклассы. Параметр metaclass

#Создание метакласса в виде функции
#Функция-метакласс должна иметь три параметра: name – имя создаваемого класса;
# base – кортеж из базовых классов; attrs – словарь с атрибутами класса.

def create_class_point(name, base, attrs):
    #Добавление атрибутов
    attrs.update({'MAX_COORD' : 100, 'MIN_COORD' : 0})
    #Вызываем метакласс, формируем новый класс и возвращаем его
    return type(name, base, attrs)

#Чтобы эта функция использовалась в качестве метакласса, при объявлении класса нужно
#прописать специальный параметр metaclass и передать ссылку на эту функцию

class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())

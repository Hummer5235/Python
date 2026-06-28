# Магические методы __str__ и __repr__
# Отвечают за текстовое отображение объекта в системе
#__str__() –  для пользователей (например, для функций print, str);
#__repr__() –  в режиме отладки (для разработчиков).
class Lion:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f'The object Lion - {self.name}'
    
    def __str__(self):
        return f'Lion - {self.name}'
    
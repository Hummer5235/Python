#Изменение атрибута класса делается через метод класса
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
    
    # Для изменения атрибута класса нужна ссылка на класс
    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left
  

    
    
pt = Point(1,2)
pt = Point(10,20)



#23. Наследование. Атрибуты private и protected
'''
_attribute (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех его
дочерних классах)
__attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса).

'''

class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2, fill=None):
        print(f'Инициализатор Geom для {self.__class__}')
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def _verify_coord(self, coord):
        return 0 <= coord < 100



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill = 'red'):
        print('Инициализатор Rect')
        if self._verify_coord(x1):
            super().__init__(x1, y1, x2, y2) # Вызываем инициализатор базового класса


        self.__fill = fill



r = Rect(10, 0, 10, 20)
print(r.__dict__)
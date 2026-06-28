#14 Магические методы __add__, __sub__, __mul__, __truediv__
'''
__add__() – для операции сложения;
__sub__() – для операции вычитания;
__mul__() – для операции умножения;
__truediv__() – для операции деления.
'''

class Clock:
    __DAY = 86400
    
    def __init__(self, seconds:int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целыми')
        self.seconds = seconds % self.__DAY
        
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = ( self.seconds // 3600 )  % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'
    
    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2,'0')
    
    def __add__(self, other):
        #Если необходимо изменить действия в классе при сложении
        print('метод __add__')
        if isinstance(other, int):
            return Clock(self.seconds + other)
            
        elif isinstance(other, Clock):
            sc = other.seconds
            return Clock(self.seconds + sc)
            
        else:
            raise ArithmeticError('Правый операнд должен быть int')
    
    def __radd__(self, other):
        #Используется когда экз кдасса прибавляется справа
        print('метод __radd__')
        return self + other
    
    def __iadd__(self, other):
        print('вызов __iadd__')
        #iadd определяет операцию +=
        #К примеру c1 = Clock(), c1 += 100, c2
        
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        self.seconds += sc
        return self
        


c1 = Clock(1006)
# c1.seconds += 100
c2 = Clock(500)
print(c1.get_time())

c1 += 1
print(c1.get_time())

c1 += c2
c3 = c1+c2
print(c1.get_time())

c4 = 100 + c1







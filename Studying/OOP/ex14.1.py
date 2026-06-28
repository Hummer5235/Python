class Clock:
    __DAY = 86400
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целыми')
        self.seconds = seconds % self.__DAY
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'
    
    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, '0')
    
    def __sub__(self, other):
        if type(other) in (int, Clock):
            if other <= self.seconds:
                if type(other) == int:
                    return Clock(self.seconds - other)
                else:
                    return Clock(self.seconds - other.seconds)
            else :
                if type(other) == int:
                    return Clock(other -self.seconds)
                else:
                    return Clock(other.seconds - self.seconds )
                
        else:
            raise TypeError('Правый операнд должен быть числом или объектом класса Clock')
            
    def __isub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int')
    
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
    
        self.seconds -= sc
        return self
        
    def __rsub__(self, other):
        return self - other
    

        
c1 = Clock(500)
c2 = Clock(1400)
# c1 -= 5
# c1 -= c2
print(c1.seconds)
c1 = 800 - c1
c2 -= 400
c2 -= c1

print(c1.get_time())
print(c2.get_time())
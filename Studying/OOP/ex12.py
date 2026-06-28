#12. Магический метод __call__. Функторы и классы-декораторы
#dunder - методы от англ. double underscore

#Магический метод __call__
'''
В действительности, когда происходит вызов класса, то автоматически запускается
магический метод __call__ и в данном случае он создает новый экземпляр этого класса:
'''

"""
c = Counter()

def __call__ (self, *args, **kwargs):
        obj = self.＿new＿(self, *args, **kwargs)
        self.＿init＿(obj, *args, **kwargs)
        return obj
"""

#Функторы - это классы с определённым оператором(). Мы сможем вызвать экз класса

class Counter:
    
    def __init__(self):
        print('вызов метода __init__')
        self.__counter = 0
    
    def __new__(cls, *args, **kwargs):
        print('вызов метода __new__')
        return super().__new__(cls)
        
    def __call__(self, step = 1, *args, **kwargs):
        print('вызов метода __call__')
        self.__counter += step
        return self.__counter
    
    
c = Counter()
c2 = Counter()

"""Благодаря методу __call__, мы можем вызывать экземпляры класса подобно функции"""
c()
c(2)
res = c(10)
res2 = c2(-5)

print(res, res2)




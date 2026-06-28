#19. Магические методы __iter__ и __next__
'''
__iter__(self) – получение итератора для перебора объекта;
__next__(self) – переход к следующему значению и его считывание.
'''
#Итератор - некий интерфейс для перебора любого итерируемого объекта. У него имеется магический метод next

class FRange:
    def __init__(self, start = 0.0, stop=0.0, step = 1.0):
        self.start = start
        self.stop = stop
        self.step = step
        
        
        
    def __iter__(self):
        self.value = self.start - self.step
        return self
        
        
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
        
fr = FRange(0 , 2, 0.5)
print(fr.value)
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))
'''
__len__() – позволяет применять функцию len() к экземплярам класса;
__abs__() - позволяет применять функцию abs() к экземплярам класса.
'''

class Point:
    def __init__(self, *args):
        self.__coords = args
        
    def __len__(self):
        return len(self.__coords)
    
    def __abs__(self):
        return list(map(abs,self.__coords))
    
    
p = Point(1,2,-3,4,-5,6,7)
print(len(p))
print(abs(p))
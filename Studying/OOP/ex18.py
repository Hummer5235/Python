#18. Магические методы __getitem__, __setitem__ и __delitem__
'''
__getitem__(self, item) – получение значения по ключу item;
__setitem__(self, key, value) – запись значения value по ключу key;
__delitem__(self, key) – удаление элемента по ключу key.
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __getitem__(self, item):
        if 0< item < len(self.marks) :
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')
    
    def __setitem__(self, key, value):
        if not isinstance(key, int) and key > 0 :
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
            
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) :
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        del self.marks[key]
    
    
s1 = Student('Григорий', [5,3,4,5,5,4])
print(s1[2])
# s1[2] = 3
s1[10] = 5
del s1[3]
print(s1.marks)
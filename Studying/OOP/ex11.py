#11. Дескрипторы (data descriptor и non-data descriptor)
'''
Дескриптор - Это класс, который содержит или один магический метод __get__
Или класс, в котором дополнительно прописаны методы __set__ и/или __del__
эти магические методы, по сути, геттеры и сеттеры, а также делитер. Давайте, теперь посмотрим,
как дескриптор может упростить наш программный код с обработкой координат точек.

'''
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    



#Класс Integer - data descriptor дескриптор данных
class Integer:
    
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')
    
    #self - Ссылка на создаваемый экземпляр класса
    #owner - Ссылка на сам класс Point3D
    #name - Имя куда сохраняется экземпляр класса x = Integer() . Через name создаем локальное св-во self.name
    
    def __set_name__(self, owner, name):
        self.name = '_' + name
        #self.x = '_x'
    
    #instance ссылается на экз класса Point из которого этот дескриптор был вызван pt = Point(1, 2, 3)
    def __get__(self, instance, owner):
        #return instance.__dict__[self.name]
        return getattr(instance, self.name)
        
        
    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

'''
Эти атрибуты (x, y, z) и есть дескрипторы данных, через которые будет проходить взаимодействие. Итак, когда мы создавали 
экземпляры классов Integer, то автоматически вызывался магический метод __set_name__
'''
 
class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    #Приоритет обращения к локальному св-ву такой же как и к дескриптору неданных
    xr = ReadIntX()
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
p = Point3D(1, 2, 3)
p.__dict__['xr'] = 5
print(p.xr,p.__dict__)
#Приоритет обращения к дескриптору данных выше чем к локальным атрибутам экземпляра класса


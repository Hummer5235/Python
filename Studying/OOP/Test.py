from accessify import private, protected

class Person:
    def __init__(self, fio, age, gender):
        
        self.validate_fio(fio)
        
        self.__fio = fio
        self.__age = age
        self.__gender = gender
    
    @classmethod
    def validate_fio(cls, fio):
        if type(fio) != str or len(fio.split()) != 3:
            raise TypeError("ФИО должно быть строкой и состоять из 3х слов")
    
    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio(self, fio):
        if type(fio) == str and len(fio.split())==3:
            self.__fio = fio
        else:
            raise TypeError("ФИО должно быть строкой и состоять из 3х слов")
    
    
            
        
p1 = Person('Герцин Алексей Иванович', 35, 'man')



    
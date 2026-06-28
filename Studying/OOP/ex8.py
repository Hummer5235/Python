#8. Паттерн "Моносостояние"
# Все экземпляры класса имеют одинаковые атрибуты, изменение атрибутов одного экземпляра
# приводит к изменению атрибутов других экземпляров

class ThreadData:
    #Словарь с общими локальными св-вами экземпляров класса
    __shared_attrs = {
        'name':'thread_1',
        'data':{},
        'id':1
    }
    
    def __init__(self):
        self.__dict__ = self.__shared_attrs
        
        
th1 = ThreadData()
th2 = ThreadData()
print(th2.name)
th1.name = 'new_name'
print(th2.name)

th1.new_attr = 'new_attr'
print(th2.__dict__)
#25. Множественное наследование

'''
Класс MixinLog работает совершенно независимо от классов Goods и Notebook и лишь добавляет функционал по логированию товаров
с использованием их id. Такие независимые базовые классы и получили название миксинов – примесей.
'''

'''
MRO – Method Resolution Order - специальный алгоритм обхода базовых классов при множественном наследовании
Мы можем увидеть эту цепочку обхода базовых классов, если распечатать специальную коллекцию __mro__ любого класса:
'''

class Goods:
    def __init__(self, name, weight, price):
        super().__init__() # Вызов инициализатора базового клаccа
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name} , {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id} товар был продан в 00:00 часов ')

    def print_info(self):
        print(f'print_info из MixinLog')


class NoteBook(Goods, MixinLog):
    pass
    # Второй вариант вызова одинакового метода из другого базового класса
    #def print_info(self):
        #MixinLog.print_info(self)

n = NoteBook('Acer', 1.5, 30000)
n.print_info()
#Первый вариант вызова одинакового метода из другого базового класса
#MixinLog.print_info(n)
n.save_sell_log()
print(NoteBook.__mro__)


#__mro__
'''
То есть, методы сначала ищутся в самом классе NoteBook, затем, в классе Goods, далее идет класс MixinLog и от него
уже идет к классу object. Это цепочка обхода для нашего конкретного примера. 
'''

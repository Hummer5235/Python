# __new__() - вызывается перед созданием объекта класса
#     |
#     |
# Объект класса
#     |
#     |
# __init__() - вызывается сразу после создания объекта класса

# cls - ссылка на текущий класс
# __new__ должен возвращать адрес нового созданного объекта
# Для этого вызываем метод __new__ из базового класса


# Класс должен быть реализовам с учетом принципа Singleton (Можно создавать только 1 экз класса)
class DataBase:
    __instance = None # Ссылка на экз класса
    
    #Переопределим метод __new__ чтобы ссылка возвращалась в атрибут класса __instance
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
        
    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')
        
    def close(self):
        print('закрытие соединения с БД')
    
    def read(self):
        return 'данные из БД'
    
    def write(self, data):
        print(f'запись в БД {data}')


db  = DataBase('root', '1234', 80)
db2  = DataBase('root2', '5678', 40)

print(id(db), id(db2))
db.connect()
db2.connect()
#Singleton - это паттерн проектирования, гарантирующий, что у класса будет только один экземпляр.



class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соедние с БД {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        print('Чтение из БД')

    def write(self,data):
        print(f'Запись в БД {data}')


db = DataBase('admin','1234',80)
db2 = DataBase('admin2','1212',40)
print(id(db),id(db2),sep='\n')

db.connect()
db2.connect()



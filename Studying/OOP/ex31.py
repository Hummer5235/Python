#31. Инструкция raise и пользовательские исключения
'''
После оператора raise мы указываем объект, который является одним из классов исключения
Таким образом мы будем генерировать исключение

'''

class PrintData:
    #Печать данных
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    #Отправление данных в принтер
    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception('Принтер не отвечает')

    #Проверка возвожности отправки данных
    def send_to_print(self, data):
        return False

p = PrintData()
p.print('123')

#31. Инструкция raise и пользовательские исключения
'''
После оператора raise мы указываем объект, который является одним из классов исключения
Таким образом мы будем генерировать исключение

'''

#Создание пользовательских исключений
'''
Мы создали новый тип исключения, просто прописав новый класс. И благодаря этому можем 
отличить ошибку передачи данных принтеру от каких-либо других ошибок.
Кроме того, мы можем расширить функционал класса ExceptionPrintSendData
'''
class ExceptionPrint(Exception):
    """Общий класс исключений принтера"""



class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


class PrintData:
    #Печать данных
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    #Отправление данных в принтер
    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не отвечает')

    #Проверка возвожности отправки данных
    def send_to_print(self, data):
        return False

p = PrintData()
p.print('123')

try:
    p.print('123')
except ExceptionPrintSendData:
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати')

"""
Это лишь пример расширения функционала класса исключения. В каждом конкретном случае программист 
может написать любую свою реализацию.Пользовательские классы исключений дают возможность создавать
свою иерархию исключений. В частности, в нашем примере, мы прописали общий класс исключений
для принтера ExceptionPrint
"""
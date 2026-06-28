# Работа с файлами
# Функция open(file,[mode = 'r', encoding = None,..] )- Для открытия файлов


# file - путь к файлу (вместе с его именем)
# mode - режим доступа к файлу (чтение/запись)
# encoding - кодировка файла

# Метод read() - чтение данных


file = open('test.txt', encoding = 'utf-8')

# print(file.read())

print(file.tell()) # Узнать файловую позицию


file.seek(0)  # Установить файловую позицию

print(file.readline()) # Прочитать строку
  


file.seek(0)
text = file.read()

file.seek(0)
s = file.readlines() 
for i in s:
	print()



file.close() # Закрыть файл


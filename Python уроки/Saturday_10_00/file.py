# f = open(file_name, access_mode)
# file_name - имя файла 
# access_mode - режим открытия файла
# 'r' - только чтение
# 'w' - только для записи. Создает новый файл, если не нашел
# 'r+' - для чтения и записи
# 'w+' - для чтения и записи. Создает новый файл, если не нашел

f = open('example.txt','w+')
#print(*f)
 # метод для чтения

f.write('Hello everyone!')
f.write('Hello ev')
f.seek(0) # Переместить указатель
print(f.read())


#работа с файлом 
f.close() # закрытие файла


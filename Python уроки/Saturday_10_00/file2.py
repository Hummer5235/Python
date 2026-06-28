import time

file = open('Зимний_вечер.txt',encoding='utf-8')
length = len(file.readlines()) # Узнать кол-во строк в файле
file.seek(0) # Переместить курсор в начало


for i in range(length):
	print(file.readline()) # Вывести построчно
	time.sleep(1)


file.close()
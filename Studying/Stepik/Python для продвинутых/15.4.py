#Функции как объекты

def start():
	print('Функция start')
	

def stop():
	print('Функция stop')


def pause():
	print('Функция pause')



commands = {'start':start,'stop':stop,'pause':pause}


command = input('Введите команду: ')
commands[command]()






#Функции в качестве аргументов других функций
numbers = [10,-7,24,13,-2,17,6,19,-37,20,12,5]
print(max(numbers,key=abs))

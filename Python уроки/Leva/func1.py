#Функция - именованный блок кода, к которому можно 
# обратиться из любого места программы

#def - declare function - объявить функцию
#hello - имя функции
#

def hello():
	print('Hello')

# hello() # вызов функции


def hello2(name):
	print(f'Hello {name}')

hello2("Leva")
hello2('Max')
hello2('Hello')
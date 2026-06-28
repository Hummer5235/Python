#Области видимости переменных

#Глобальная переменная - переменная доступная в любом месте программы
a = 10
B = 'hello'
WIDTH, HEIGHT = 1000, 800 

#Локальная переменная - это переменная созданная внутри функции


def myFunc(b):
	global a
	lst = [] #Локальная переменная
	# a = 5
	for x in range(b):
		n = x+1
		print(n,end=' ')
		print('Переменная а:',a)

myFunc(5)

# print(lst)
print('Переменная а:',a)





name = 'Alex' #Глобальная переменная

def say_hi():
	print(f'Hi {name}')

def say_bye():
	name = 'Bob' # Локальная переменная
	print(f'Good bye {name}')

say_hi()
say_bye()


def hello(name='Andrey'):
	print(name)

hello('Alex')
hello()
# Если внутри функции мы хотим использовать и менять глобальную пременную, необъодимо указать global ...

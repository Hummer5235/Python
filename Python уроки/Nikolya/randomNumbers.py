#import ... Для подключения модуля
import random

x = random.randint(0,10) 

while True:
	number = int(input('Введите число: '))
	if number == x:
		break

print(f'Молодец, ты угадал! Это было число {x}')



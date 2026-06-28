number = int(input('Введите число: '))


last_last_number = 0
while number != 0:

	last_number = number % 10
	print(last_number,last_last_number)
	number = number // 10
	if number != 0 :
		last_last_number = last_number

print('Предпоследнее число:',last_last_number)


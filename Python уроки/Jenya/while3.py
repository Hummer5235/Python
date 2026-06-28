
price = int(input('Введите стоимость услуги: '))
count = 0

while price != 0 :
	if price - 25 >=0:
		price -=25
		count += 1
	elif price - 10 >=0:
		price -=10
		count += 1
	elif price - 5 >=0:
		price -= 5
		count += 1
	elif price - 1 >=0:
		price -=1
		count += 1
print(f'Количество {count}')
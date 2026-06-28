def is_valid(data):
	if data.isdigit() and 1<= int(data) <= 100:
		return True
	else:
		return False

while True:
	n = input('Введите число от 1 до 100: ')
	if is_valid(n):
		n = int(n)
	else:
		print('А может быть все-таки введем целое число от 1 до 100?')

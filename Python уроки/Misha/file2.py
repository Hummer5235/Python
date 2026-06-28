
try:
	file = open('test.txt', encoding = 'utf-8')

	try:
		s = file.readlines()

	finally:
		file.close()
		print('Файл закрыт? ',file.closed)


except FileNotFoundError:
	print('Невозможно открыть файл')



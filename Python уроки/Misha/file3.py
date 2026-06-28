#Менеджер контекста автоматически закрывает файл при завершении работы с ним

try:
	with open('test2.txt',encoding = 'utf-8') as file:
		print('Файл закрыт? ',file.closed)

		s = file.readlines()
		
		print(s)


except FileNotFoundError:
	print('Невозможно открыть файл')


print('Файл закрыт? ',file.closed)

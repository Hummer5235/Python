import re

password = input('Введите пароль: ')


def	validatePassword(password):
	lst_valid = ['[A-Z]','[a-z]','\d']
	counter = 0
	simbol_counter = 0
	for i in lst_valid:
		lst = re.findall(i,password)
		if len(lst)>0:
			counter+=1
			simbol_counter+= len(lst)

	print(counter)
	if counter == 3:
		print('Пароль принят!')
	elif simbol_counter<8:
		print('Длина пароля должна быть не меньше 8 символов')
	elif counter <3:
		print('Пароль введен некорректно. Используйте 8 символов , большие и малые буквы. Также цифры')

validatePassword(password) 




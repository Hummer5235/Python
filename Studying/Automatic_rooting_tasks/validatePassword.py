import re

password = input('Введите пароль: ')


def	validatePassword(pas):
	lst = re.findall(r'[[A-Z]+[a-z]+\d+]',pas)
	if lst == []:
		print('Пароль введен некорректно. Используйте 8 символов , большие и малые буквы. Также цифры')
	elif len(lst[0])<8:
		print('Длина пароля должна быть не меньше 8 символов')
	print(lst)

validatePassword(password) 



r'[A-Z]+[a-z]+\d+'
r'[[A-Z]+[a-z]+\d+]'
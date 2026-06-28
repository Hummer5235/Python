birthdays = open('birthdays.txt','r+',encoding ='utf-8')

spisok= birthdays.read()
print(spisok,type(spisok))


while True:
	name = input('Введите имя (пробел для выхода): ')
	if name == ' ':
		break

	
	if name in dictionary:
		
		print(f'День рождения {name}: {dictionary[name]}')
		

	else:
		new_birthday = input('Введите дату рождения: ')
		dictionary[name] = new_birthday
		
		birthdays.write(dictionary)
	
	

	
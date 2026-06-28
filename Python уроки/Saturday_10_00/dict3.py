import pickle


birthdays = {'Марина':'23 октября','Гриша':'23 июня'}
file = open('birthdays.bin','wb')
pickle.dump(birthdays,file) # Записать в файл


#Загружаем данные из файла
file = open('birthdays.bin','rb')
birthdays = pickle.load(file)


while True:
	name = input('Введите имя (пробел для выхода): ')
	if name == ' ':
		break

	if name in birthdays:
		print(f'День рождения {name}: {birthdays[name]}')

	else:
		birthday_data = input('Введите дату рождения: ')
		birthdays[name] = birthday_data
		#Добавляем данные в файл
		file = open('birthdays.bin','wb')
		pickle.dump(birthdays,file)
		file.close()
	
	print(birthdays)



	
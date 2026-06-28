import pickle


birthdays = {'Марина':'23 октября','Гриша':'23 июня'}
file = open('birthdays.txt','a')
pickle.dump(birthdays,file)
file.close()
# data = file.read()

#Загружаем данные из файла
file = open('birthdays.txt','r')
birthdays = pickle.load(file)
file.close()

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
		file = open('birthdays.txt','w')
		pickle.dump(birthdays,file)
		file.close()
	
	print(birthdays)
	print()


	
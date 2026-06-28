import pickle
import time 

#Загружаем данные в файл

# birthdays = {'Марина':'23 октября','Гриша':'23 июня'} # Начальный список дней рождений
# file = open('birthdays.bin','wb')
# pickle.dump(birthdays,file) 



#Выгружаем данные из файла
file = open('birthdays.bin','rb')
birthdays = pickle.load(file)
file.seek(0)


def loading():
	time.sleep(0.5)
	print("....")
	time.sleep(0.5)
	print("...")
	time.sleep(0.5)
	print("....")
	time.sleep(0.5)


print("Имена в списке:")
for i in birthdays:
	print(f'-{i}')

print()





while True:
	name = input('Введите имя (пробел для выхода): ')
	if name == ' ' or name =='' :
		break

	
	if name in birthdays:
		
		print(f'День рождения {name}:{birthdays[name]}')
		print()
		

	# Если имени нет в словаре
	else:
		new_birthday = input('Введите дату рождения: ')
		print()
		birthdays[name] = new_birthday

		# Добавляем данные в файл
		file = open('birthdays.bin','wb')
		pickle.dump(birthdays,file)
		file.close()




loading() #
print()
print('Дни рождения: ')
for i in birthdays:
	print(f'-{i}',birthdays[i])

print()

while 1:
	answer = input('Хотите что-нибудь удалить? ')
	if answer.lower() == 'да' :
		name = input('Введите имя: ')
		if name in birthdays:
			del birthdays[name] #  Удаление из словаря
			# Добавляем данные в файл
			file = open('birthdays.bin','wb')
			pickle.dump(birthdays,file)


		else:
			loading()
			print('Такого имени нет в списке, попробуйте еще раз')
			print()

	else:
		loading()
		print('Программа завершена')
		break






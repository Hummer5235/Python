birthdays = {"Santa":"1 January","Misha":"19 September"}

while True:
	print("Введите имя: ")
	name =input()
	if name =="":
		break

	if name in birthdays:
		print(f"{birthdays[name]} День рождения у {name}")

	else:
		print(f"У меня нет информации о Дне рождения {name}")
		print("Когда у него День рождения?")
		bday = input()
		birthdays[name] = bday
		print("\nБаза обновлена",end="\n\n")

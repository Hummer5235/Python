name = input("Введите свое имя: ")
age = int(input("Введите свой возраст: "))


if age > 18 :
	password = input("Введите пароль для входа: ")
	if password == "Qwerty":
		print("Пароль верный!")
	else:
		print("Пароль неверный!")
else:
	print("Вы не подходите по возрасту")


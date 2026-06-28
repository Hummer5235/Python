
#break -oператор прерывания цикла

# while True:
# 	name = input("Введите имя: ")
# 	print(f"Привет {name}")

# 	if name=="Сева" or name=="Миша":
# 		print("Извините , вы не проходите")
# 		break


#continue - оператор начинает следующее повторение, а код после него не выполняется
while True:
	name = input("Введите имя: ")

	if name=="Хакер":
		print("Ошибка")
		continue
		print("Ну ты ващеееее")

	print(f"Привет {name}")
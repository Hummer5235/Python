Timur = input()
Ruslan = input()
if Timur =="камень":
	if Ruslan =="бумага":
		print("Руслан")
	elif Ruslan == "камень":
		print("ничья")
	else:
		print("Тимур")
elif Timur =="ножницы":
	if Ruslan =="бумага":
		print("Тимур")
	elif Ruslan == "камень":
		print("Руслан")
	else:
		print("ничья")

else :
	if Ruslan =="бумага":
		print("ничья")
	elif Ruslan == "камень":
		print("Тимур")
	else:
		print("Руслан")
age = int(input("Введите ваш возраст: "))
if age < 10:
	print("Ты еще мал!")
elif age < 18:
	print("Ты еще учишься в школе")
elif age < 24:
	print("Ты еще учишься в институте")
else:
	print("Где ты работаешь?")
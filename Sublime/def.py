def math(a,b):
	if a > b:
		return True
	elif a < b:
		return False

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


if math(a,b)== True:
	print("Первое число больше второго")
if math(a,b)==False:
	print("Первое число меньше второго")

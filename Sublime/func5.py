#Функция квадрат
def sq(a):
	return a**2
for i in range(5):
	b=int(input("Введите число: "))
	c=sq(b)
	print(f"{b} в квадрате равно {c}")

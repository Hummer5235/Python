print("Для выхода из цикла введите 0")
n = int(input("Введите число: "))
counter = 1
summ = 0

while n != 0 :
	n = int(input("Введите число: "))
	counter += 1 # Увеличение числа попыток
	summ += n

print(f"Количество попыток: {counter}")


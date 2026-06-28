
print("Здесь загадано секретное число")
n = int(input("Введите число: "))

count = 1 # счетчик попыток

while n != 0:
	n = int(input("Введите число: "))
	count += 1
	
print(f"Вы ввели верное число {n}")
print(count)


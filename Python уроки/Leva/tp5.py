numbers = [10,15,3,21,74,5,4,14]
a = numbers[0]
for number in numbers:
	if number > a:
		a = number
print(f"Максимальное значение списка: {a}")

numbers = [10,15,3,21,74,5,4,14]
a = numbers[0]
for number in numbers:
	if number < a:
		a = number
print(f"Минимальное значение списка: {a}")
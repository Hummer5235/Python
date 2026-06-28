# #Сумма чисел списка
# #Среднее арифметическое чисел списка
# numbers = [13, 12, 1, 24, 37, 45]

# summa = 0
# for number in numbers:
# 	summa += number

# print(f'Сумма чисел списка: {summa}')
# print(f'Среднее арифметическое чисел списка: {summa/len(numbers)}')




numbers = [13, 120, 100, 24, 37, 45]

minimum = numbers[0]

for i in numbers:
	if i < minimum:
		minimum = i

print(f'Минимальное число: {minimum}')


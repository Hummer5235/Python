n = int(input())
numbers = []
for i in range(n):
	a = int(input())
	numbers.append(a)
b = int(input())

exitFlag = False
for i in range(numbers):
	new_lst = numbers[0:i]+numbers[i+1:]
	for j in new_lst:
		if numbers[i]*j == b:
			exitFlag = True

if exitFlag:
	print("ДА")
else:
	print("НЕТ")
			

n = int(input("Количество чисел: "))
numbers = []
for i in range(n):
	a = int(input("Число: "))
	numbers.append(a)
b = int(input("Число для проверки: "))
for i in range(len(numbers)):
	new_lst = numbers[0:i]+numbers[i+1:]
	print(new_lst)

K = int(input("Введите первое число: "))
N = int(input("Введите первое число: "))
sum=0
count=0
for i in range(K,N+1):
	sum+=i
	count+=1
print(f"Сумма чисел равна {sum}")
print(f"Среднее арифметическое чисел равно {sum/count}")


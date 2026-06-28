k = int(input())
n = int(input())
summa = 0
print()

for i in range(k,n+1):
	print(i)
	summa += i
print(f"Сумма всех чисел от {k} до {n} равна: {summa}")


k = int(input("Введите число: "))
n = int(input("Введите число: "))

sum = 0
for i in range(k,n+1):
 	if i%2 == 0:
 		print(i)
 		sum+=i
print(f"\nСумма чисел от {k} до {n}, равна {sum}")

sum=0
print('#Ввод')
N = int(input("Введите число: "))

for i in range(1,N+1):
	l=1+i/10
	sum+=l
print('#Вывод')
print("Сумма чисел равна", sum)

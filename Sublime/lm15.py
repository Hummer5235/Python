#Уникальная последовательность элементов
N=int(input("Введите количество чисел: "))
strings=[]
for i in range(N):
	strings.append(input("Введите число: "))
print(strings)

for idx in range(len(strings)):
	strings[idx]=int(strings[idx])
print(strings)

for i in strings:
	n=strings.count(i)
	if n !=1:
		for j in range(n-1):
			strings.remove(i)
print(strings)
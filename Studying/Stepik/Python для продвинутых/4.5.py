#Таблица умножения

n = int(input())
m = int(input())

mult = []

for i in range(n):
	mult.append([])
	for j in range(m):
		mult[i].append(i*j)

print(mult)

for i in mult:
	for j in i:
		print(str(j).ljust(3),end ='')
	print()
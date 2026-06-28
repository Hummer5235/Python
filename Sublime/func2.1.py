draggun=0
name = "Vasya"
N=int(input("Введите число: "))
for i in range(N):
	A=int(input("Введите число: "))
	spisok.append(A)
	for o in range(A):
		if i<10:
			draggun+=1
print(draggun)

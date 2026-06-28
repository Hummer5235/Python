#Ряд Фибоначчи
N = int(input("Введите число: "))
i=0
a=0
b=1


while i<N-1:
	c=a+b
	a=b
	b=c
	i+=1

print(b)
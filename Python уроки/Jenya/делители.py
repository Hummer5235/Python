number = int(input('Введите число:'))

for j in range(1,number+1):
	counter = 0
	c = j
	for i in range(1,j+1):
		if j%i==0:
			counter+=1
	print(j,'+'*counter)

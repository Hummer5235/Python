N=int(input("Введите кол-во чисел для записи: "))

data=input('Вводите числа через запятую:').split(",")
print(data)


for i in range(N):
	data[i]=int(data[i])
print(data)

sum=0
for i in data:
	if i<10:
		sum+=1
print(sum)

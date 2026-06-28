#Вариант 1
N=int(input("Введите кол-во чисел для записи: "))

numbers=[]

for i in range(N):
	a=int(input("Введите число: "))
	numbers.append(a)
print(numbers)

#Вариант 2
N2=int(input("Введите кол-во чисел для записи: "))

numbers2=[]

for i in range(N2):
	numbers2.append(input("Введите число: "))

for i in range(len(numbers2)):
	numbers2[i]=int(numbers2[i])
print(numbers2)


# m=numbers[0]
# for j in numbers:
# 	if j>=m:
# 		m=j
# print(m)
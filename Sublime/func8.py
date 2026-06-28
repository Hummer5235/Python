#Сумма элементов списка
c=[1,3,4,5,77]
numbers=list(range(11))

def sum_lst(list):
	sum=0
	for i in list:
		sum+=i
	return sum
#Приведение элементов списка к целочисленному типу данных
def int_lst(list):
	for i in range(len(list)):
		list[i]=int(list[i])
	return list

print(sum_lst(numbers))

print(sum_lst(c))
d=input("Введите числа через пробел: ").split(" ")
d=int_lst(d)
d=sum_lst(d)
print(d)



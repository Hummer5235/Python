#Количество нечетных элементов списка
def not_even(list):
	qua=0
	for i in list:
		if i%2==0:
			qua+=1
	return qua

numbers=[1,10,15,3,21,5,74,92]
numbers2=list(range(100))
print(not_even(numbers))
print(not_even(numbers2))


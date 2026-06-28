#Количество повторяющихся элементов списка
lst=[1,2,3,1,2,4,5,7]
lst2=[]
sum=0
def only_one(list):
	for i in list:
		if list.count(i)==1:
			global sum
			sum+=1
	return sum

print(only_one(lst))




import this 
# Сложение списков
def int_lst(list):
	for i in range(len(list)):
		list[i]=int(list[i])
	return list


def sum_lst(lst1,lst2):
	if len(lst1) != len(lst2):
		return -1
	else:
		lst3=list()
		for i in range(len(lst1)):
			lst3.append(lst1[i]+lst2[i])
	return lst3

list1=input("Введите числа через пробел: ").split()
list2=input("Введите числа через пробел: ").split()
list1=int_lst(list1)
list2=int_lst(list2)


print(sum_lst(list1,list2))
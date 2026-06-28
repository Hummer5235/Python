

def create_list():
	lst = [1,2,3]
	return lst


lst1 = create_list()
lst2 = create_list()

print(lst1, lst2)



#------------------------------------------------------

def ListFromInput():
	lst = []
	for i in range(5):
		a = int(input("Введите число: "))
		lst.append(a)
	return lst

list1 = ListFromInput()
print(list1)
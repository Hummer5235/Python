def ListFromInput(n):
	lst = []
	for i in range(n):
		item = input("Введите число: ")
		lst.append(item)
	return lst

mylst = ListFromInput(5)
print(mylst)


mylst2 = ListFromInput(3)
print(mylst2)


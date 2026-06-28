def listFromInput(n):
	lst =[]
	for i in range(n):
		item = int(input("Введите число: "))
		lst.append(item)
	return lst

mylst = listFromInput(2)
print(mylst)

mylst2 = listFromInput(5)
print(mylst2)

mylst3 = listFromInput(1)
print(mylst3)
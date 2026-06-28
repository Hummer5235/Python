

def findMax(lst):
	maximum = lst[0]
	for item in lst:
		print(item)
		if item> maximum:
			maximum = item
	return maximum

mylst = [-10,-23,-43,-1,-5]
mymax = findMax(mylst)
print("Max: "+ str(mymax))


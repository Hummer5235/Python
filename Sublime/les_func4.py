def find_max(spisok):
	maximum = spisok[0]
	for i in spisok:
		if maximum < i:
			maximum = i
	return maximum

a = [1,2,3,4,5,6,7]
b = [1,20,3,4,15,6,7]
c = [1,21,3,43,5,62,7]

print(find_max(a))
print(find_max(b))
print(find_max(c))
string = input().split()
lst = list(map(int,string))

saldom_numbers = []

for i in lst:
	if not i in saldom_numbers:
		saldom_numbers.append(i)

print(len(saldom_numbers))


string = input()
counter = 1
lst = []
for idx in range(len(string)):
	if string[idx] == "Р" and idx+1<len(string):
		if string[idx] == string[idx+1] :
			counter += 1
	else:
		lst.append(counter)
		counter = 1

if "Р" in string:
	print(max(lst))
else:
	print(0)


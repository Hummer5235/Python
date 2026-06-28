string = input() 
new_string = ""
n = 0
if len(string) > 3:
	for i in range(len(string)-1,-1,-1):


		new_string += string[i]
		n += 1
		if n == 3:
			new_string += ","
			n = 0
	if new_string[-1] == ",":
			new_string = new_string[:-1]
	new_string = new_string[-1::-1]
	
	print(new_string)

else:
	print(string)

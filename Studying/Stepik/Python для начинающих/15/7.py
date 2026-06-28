#Перевод в десятичную систему счисления

def system(number, num_sys):
	new_number = 0
	number = str(number)
	for i in range(len(number)):
		new_number += int(number[i])*num_sys**(len(number)-i-1)
	return new_number


print(system(111111,2))
print(system(88,9))

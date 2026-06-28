number = input()
new_number = ""
for idx in range(len(number)):
	if idx % 2 == 0 and idx != 0 :
		new_number += ","
	new_number += number[idx]
print(new_number)

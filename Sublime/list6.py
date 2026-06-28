N = int(input("Введите количество элементов: "))
List = input("Введите числа через пробел: ").split(" ")


def int_list(list):
	for i in range(len(list)):
		list[i] = int(list[i])
	return list

print(int_list(List))

f="NO"
for i in range(N-1):
	if List[i] >0: 
		if List[i+1]<0:
			f="NO"
	elif List[i] <0 and List[i+1]>0:
		f="NO"
	else:
		f="YES"
		break
print(f)

#Факториал числа
def fact(numb):
	s=1
	for i in range(1,numb+1):
		s*=i
	return s

print(fact(5))
print(fact(3))

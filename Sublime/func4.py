#Функции: Поиск максимума в списке
import random
def find_max(lst):
	maxx=lst[0]
	for value in lst:
		if value>maxx:
			maxx=value
	return maxx


a=[1,2,3,4,7]
b=list(range(15))
c=list(random.randint(-32,57) for i in range(20))

print(find_max(a))
print(find_max(b))
print(find_max(c))

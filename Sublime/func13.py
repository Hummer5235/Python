#Повторяющиеся элементы 2х списков
def rep(lst1,lst2):
	sum=0
	for i in lst1:
		if i in lst2:
			sum+=1
	return sum

l1=[1,2,3,4,5,6]
l2=[2,3,6,7,8,9]

print(rep(l1,l2))
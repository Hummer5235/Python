import random
from operator import *
lst = [random.randint(0,1000) for i in range(50)]
lst2 = [random.randint(0,1000) for i in range(50)]

new_lst= []
for i in range(len(lst)):
	new_lst.append(add(lst[i],lst2[i]))
print(lst,lst2)

print(new_lst)
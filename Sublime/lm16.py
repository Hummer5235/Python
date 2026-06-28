import random
numbers=[]

for  i in range(25):
	n=random.randint(-15,25)
	numbers.append(n)
m=0
for i in numbers:
	if i>=m:
		i=m

print(m)
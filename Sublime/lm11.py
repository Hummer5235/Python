import random

numbers=[]
sum=0
for i in range(10):
	n=random.randint(0,10)
	sum+=n
	numbers.append(n)
	

print(numbers)
print(sum/10)
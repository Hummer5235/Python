from random import randint

file = open('Numbers2.txt','a+')


numbers = ''
for i in range(10000):
	for i in range(3):
		numbers+= str(randint(1,9))
	numbers+='-'
	for i in range(3):
		numbers+= str(randint(1,9))
	numbers+='-'
	for i in range(4):
		numbers+= str(randint(1,9))
	numbers+='\n'
	file.write(numbers)
 
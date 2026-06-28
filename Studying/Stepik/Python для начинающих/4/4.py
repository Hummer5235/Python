import math
def pascal(number_of_string):
	lst = []
	for i in range(number_of_string+1):
		lst.append(math.factorial(number_of_string)/(math.factorial(i)*math.factorial(n-i)))
	return(lst)


	return lst

n = int(input())
print(pascal(n))
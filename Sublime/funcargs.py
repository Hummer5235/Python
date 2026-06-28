lst = []

def list():
	for i in range(5):
		i = int(input())
		lst.append(i)
	

def add_numbers(*args):
	total=0
	for a in args:
		for i in a:	
			total += i
	print(total)

list()
add_numbers(lst)




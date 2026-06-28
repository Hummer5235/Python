


def my_reduce(operation, items, initial_value):
	acc = initial_value
	for item in items:
		acc = operation(acc,item)
	return acc



def add(x, y):
	return x+y


def mult(x, y):
    return x*y


numbers = [1, 2, 3, 4, 5]

total = my_reduce(add, numbers, 0)
product = my_reduce(mult, numbers, 1)

print(total)
print(product)
import timeit

def factorial(x):
	if x == 0:
		return 1
	else:
		return x*factorial(x-1)

a = '''def factorial(x=120):
	if x == 0:
		return 1
	else:
		return x*factorial(x-1)'''


def factorial2(x):
	res = 1
	def get_number():
		nonlocal res, x
		for i in range(1,x):
			res *= x
			x -= 1 
		return res
	return get_number


# f = factorial2(20)
# print(f())

b = '''def factorial2(x=120):
	res = 1
	def get_number():
		nonlocal res, x
		for i in range(1,x):
			res *= x
			x -= 1 
		return res
	return get_number'''




print(timeit.timeit(a),'Рекурсия')
print(timeit.timeit(b),'Замыкание')






def counter():
	start = 0
	def step():
		nonlocal start
		start += 1
		return start
	return step


f1 = counter()
# print(f1())
# print(f1())
# print(f1())
# print(f1())
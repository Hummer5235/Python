

def summa(*args):
	s = 0
	for item in args:
		s += item
	return s

print(summa(5,7))
print(summa(2,15))
print(summa(2,3,8,7))
print(summa(2,3,8,7,30,13))
print(summa(2))
print(summa())


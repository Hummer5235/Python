#Глобальная переменная
a = 10

def summa():
	global a
	a += 10
	#Локальная переменная
	new = 1
	print(a)


summa()
print()


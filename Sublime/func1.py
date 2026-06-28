# Функция - многократно повторяемый блок кода с именем
# def - declare function
# hello - имя функции
# name - параметр


def hello(name):
	print("Hello",name)

hello("Ivan")
hello("Misha")
hello("Seva")

def sum2(a,b):
	return a+b  # Возврат суммы двух чисел



def sub2(a,b):
	return a-b

def mul2(a,b):
	return a*b

def div2(a,b):
	return a/b

c = sum2(10,2)
print(c)
print(sub2(10,2))
print(mul2(10,2))
print(div2(10,2))
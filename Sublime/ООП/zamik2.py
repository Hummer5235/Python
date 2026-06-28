# # Замыкания Часть 2
# # Подсчет вызова функции + среднее арифметическое

# def everage_numbers():
# 	summa = 0
# 	count = 0
# 	def inner(number):
# 		nonlocal summa,count
# 		summa +=number
# 		count +=1
# 		return summa/ count
# 	return inner

# # Вариант номер 2........................................
# # Таймер

# from datetime import datetime
# import time 

# def timer():
# 	start = datetime.now()

# 	def inner():
# 		return datetime.now()-start
# 	return inner


# from time import perf_counter

def timer():
	start = perf_counter()
	def inner():
		return perf_counter()-start
	return inner

#ДЗ
# def timer():
# 	start = perf_counter()
# 	def inner():
# 		nonlocal start
# 		b = perf_counter()
# 		c = b-start
# 		start = b
# 		return c
# 	return 

# Вариант номер 3........................................

def add(a,b):
	return a+b
def counter(func):
	count = 0
	def inner(*args,**kwargs):
		nonlocal count
		count+=1
		print(f"Функция {func.__name__} была вызвана {count} раз")
		return func(*args,**kwargs)
	return inner
a =counter(add)
print(a(2,3))
print(a(10,15))

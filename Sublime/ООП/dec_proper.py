# Декоратор 

def header(func):


	def inner(*args,**kwargs):
		print("h1")
		func(*args,**kwargs)
		print("/h1")
	return inner

def table(func):


	def inner(*args,**kwargs):
		print("table")
		func(*args,**kwargs)
		print("/table")
	return inner

#Декорирование
@header  # say = header(table(say))
@table	 # say = table(say) 

def say(*args,**kwargs):
	print("Hello,",*args,**kwargs)

def buy():
	print("Buy world!")

#say = header(table(say))  Это еще не декоратор

say("Vasya","Ivanov",30)

# При декорировании мы теряем документацию и имя передаваемой функции. Чтобы избежать этого, необходимо 
# Следующее: Добавить присвоение

def header(func):

	def inner(*args,**kwargs):
		print("h1")
		func(*args,**kwargs)
		print("/h1")
	inner.__name__ = func.__name__
	inner.__doc__ = func.__doc__
	return inner

def sqr(x):
	"""
	Функция возвращает квадрат x
	"""
	print(x**2)

# Также можно использовать декоратор @wraps
from functools import wraps
def header(func):
	@wraps(func)
	def inner(*args,**kwargs):
		print("h1")
		func(*args,**kwargs)
		print("/h1")
	return inner

def sqr(x):
	"""
	Функция возвращает квадрат x
	"""
	print(x**2)
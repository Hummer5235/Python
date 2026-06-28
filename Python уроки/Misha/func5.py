#Получение именнованных аргументов в виде словаря

def my_func(a,b,*args, name='Ivan', age = 15 , **kwargs):
	print(type(kwargs))
	print(a,b)
	print(args)
	print(name,age)
	print(kwargs)







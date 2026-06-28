#*args - параметр args получит в виде кортежа все аргументы, переданные в функцию при ее вызове от текущей позиции и до конца.

def my_func(num,*args):
	print(num)
	print(args)


# my_func(1)
# my_func(1,2,3)
# my_func('c','f')

lst = [1,2,3,4,5,6]
print(lst)
print(*lst,sep='\n') #
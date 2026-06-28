# text = input()
# s = set()
# while text!="":
# 	a = text.split()
# 	s.update(a)
# 	text = input()
# print(s)
# print(len(s))

# Задача 1

# def to_set(par):
# 	s = set(par)
# 	return s ,len(s)
	

# print(to_set([1,15,2,1,3]))
# print(to_set("я обычная строка"))


# Задача 2 
# При решении придется проверять каждый элемент списка на хешируемость. 
# Для этого воспользуемся классом Hashable из модуля collections.

# import 	collections.abc

# st = set()
# def list_to_set(lst):
# 	for i in lst:
# 		if isinstance(i,collections.abc.Hashable):
# 			st.add(i)
# 	print(st)



# list_to_set([12,"boom",132,[7,"mom"]])

# Задача 3

set1 = {1,2,3}
set2 = {2,3,4}
set3 = {5,1,9}

def diff(s1,s2,s3, symmetric = True):
	return s1^s2^s3


print(diff(set1,set2,set3))


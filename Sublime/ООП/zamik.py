
# # Замыкания - Вложенная функция пользуется переменными, которые не объявлены в ее теле.
# def main_func(name):
# 	def inner_func():
# 		print("hello my fried", name)
# 	return inner_func

# # В переменную возвращается сама функция. При этом не удаляется переменная в nonlocal 

# a = main_func()

# Вариант номер 2........................................
# Прибавление значения к заранее выбранному

# def adder(value):

# 	def inner(b):
# 		 print(value + b)
# 	return inner

# b = adder(5)
# b(10) # = 15 , т.к. value будет уже иметь значение 5

# Вариант номер 3........................................
# Подсчет вызова функции

def counter():
	count = 0
	def inner():
		nonlocal count
		count+=1
		return count
	return inner


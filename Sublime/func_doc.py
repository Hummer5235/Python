def printMax(x,y):

	"""Выводит максимальное из двух значений.

Оба должны быть целыми числами."""
	x = int(x)# конфертируем в целые числа , если возможно
	y = int(y)

	if x >y:
		print(x,"наибольшее")
	elif x<y:	
		print(y,"наибольшее")
	else:
		print("равны")

printMax(7,5)
printMax(4,4)
printMax(3,10)
print(printMax.__doc__)
help(printMax)
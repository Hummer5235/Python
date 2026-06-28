# local and global

a = 10 # определены вне функции
b = 20

def sum():
	global a # Ключевое слово
	a += 100
	с = a+b
	print("Сумма:",с)

sum()
print(a)
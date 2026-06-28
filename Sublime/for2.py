# range() - функция , возвращает последовательность чисел в некотором диапазоне

print("range(3) -> 0,1,2")
for x in range(3):
	print(x)

print("range(5) -> 0,1,2,3,4")
for x in range(5):
	print(x)

#for с двумя аргументами
print("range(5,10) -> 5,6,7,8,9")
for x in range(5,10):
	print(x)

#for с тремя аргументами
print("range(0,10,2) -> 0,2,6,4,8")
for x in range(0,10,2):
	print(x)

#for с отицательным шагом
print("range(10,0,-1) -> 10,9,8,7,6,5,4,3,2,1")
for x in range(10,0,-1):
	print(x)



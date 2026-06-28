# Списки
# Перебор значений списка

numbers = ["one","two","three"]
print("Вывод списка numbers: ")
for number in numbers:
	print(number) 

print()

print("Вывод списка names: ")
names = ["Ivan","Masha","Petr","Vasiliy"]
for i in names:
	print(i)
print()

print("Вывод списка integers: ")
integers = [1,27,15,63,88]
for i in integers:
	print(i)

#Перебор значений списка по индексам

names = ["Миша","Сева","Захар","Николай"]
l = len(names)

for idx in range(l):
	print(idx,names[idx])

# append() - добавляет элемент в конец списка
# spisok  = [10,15]
# spisok.append(100) # --> spisok [10,15,100]

# # pop() - удаляет элемент и списка по индексу . И возвращает удаленный элемент
# print(spisok.pop(0)) # --> spisok [15,100]
# spisok.pop()  # Без аргумента удаляет последний элемент --> spisok [15]
# print(spisok)

# # insert() - добавляет элемент на указанную позицию
# names = ["Ivan","Maria"]
# names.insert(0,"Artur")
# print(names)

# # remove() - удаляет элемент из списка по значению 
# fruits = ["Apple","Grape","Lemon"]
# fruits.remove("Apple") # --> fruits ["Grape","Lemon"]

# sort() - сортирует список.Вызов sort() без аргументов сортирует элементы по возрастанию.

# names = ["Maxim","Alexey","Evgeniy"]
# names.sort()
# print(names)

# numbers = [14,2,17,35,84,0]
# numbers.sort()
# print("По возрастанию", numbers)

# numbers.sort(reverse = True)
# print("По убыванию",numbers)


# list() - встроенная функция, создает список из последовательности
a  = list("список")
b = list(range(10))

print(a)
print(b)


# append - добавляет элемент в конец списка
numbers = []
numbers.append(5)
print(f"Добавили элемент 5 в список {numbers}")

# pop - удаляет элемент из списка по индексу
numbers = [4,5,21,17,45,5]
print(numbers)
numbers.pop(1)
print(numbers)

#insert - добавляет элемент на указанную позицию

names = ["Ivan","Max"]
print(names)
names.insert(0,"Kostya")
print(names)

#remove - удаляет элемент из списка по значению
numbers = [10,12,14,16,12,12]
print(numbers)
numbers.remove(12)
print(numbers)

names = ["Ivan","Max"]
print(names)
names.remove("Ivan")
print(names)



#sort - сортирует список 
names = ["Maxim","Ivan","Anton"]
print(names)
names.sort()
print(names)

numbers = [10,3,8,15,4]
print(numbers)
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)


string = "My favourite book"
list_from_string = list(string)
print(list_from_string)

splitter_string = string.split()
print(splitter_string)

string = "Hello everyone who look on me"
splitter_string = string.split("e")
print(splitter_string)
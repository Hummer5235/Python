#Добавление элементов 
#Сортировка элементов
#Метод sort()
names=["Fedor","Nikolay","Nikita"]
#Добавление элемента по индексу, список сдвигается
names.insert(0,"Dima")
names.insert(1,"Den")

print(names)

 
numbers=[]
for i in range(5):
	numbers.append(int(input("Введите число: ")))
#Сортировка элементов
numbers.sort()
print(numbers)

#Обратная сортировка
numbers.sort(reverse=True)
print(numbers)


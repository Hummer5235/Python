# Список - Непрерывная динамическая коллекция элементов. 
# Список - Последовательность пронумерованных элементов по индексам
# Список - Тип данных

numbers = [1,14,52,7]
print(numbers)

# Индекс - порядковый номер элемента списка
print("Элемент с индексом 0 равен :",numbers[0])
print("Элемент с индексом 1 равен :",numbers[1])

fruits = ["Apple","Grape","Peach","Watermelon","Orange"]
list_of_lists = [[2,4,0],[13,15,18],["Masha","Misha"]]
print(fruits[3])

print("Элемент с индексом 1 равен :",list_of_lists[1])
print("Элемент с индексом 0 внутри элемента равен :",list_of_lists[1][0])

print(fruits[-1]) # Элемент c индексом -1 дает последний эл списка
print(fruits[-2]) # Элемент c индексом -2 дает предпоследний эл списка

fruits[0] = "Orange"
print("Новые фрукты",fruits)


# Срез - позволяет получить несколько значений в виде нового списка
print(fruits[1:4])
print(fruits[2:])
print(fruits[:3])

# len() - возвращает количество значений в переданной ей последовательности 
print("Длина списка со списками",len(list_of_lists))
print("Длина списка fruits",len(fruits))


fruits = ["Apple","Grape","Peach","Watermelon","Orange"]
fruits[0],fruits[1] = fruits[1],fruits[0]
print(fruits)

a , b , c = 1 , 2 , 3
print(a , b , c)
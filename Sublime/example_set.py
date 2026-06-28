# Множество (set)
# Неупорядоченная коллекция уникальных элементов

#Создание
a = {1,2,3}
print(a,type(a))

#Множество не будет содержать повторений
a = {1,2,3,1,2,3,1,2,3}
print(a)

b = {"hi","hi","he","ho","he"}
print(b,type(b))

#Функция set
c = set("abracadabra")
print(c)

d = set([1,2,3,1,2,3])
print(d)

e = set(range(10))
print(e)

f = set()
print(f,type(f))

# Исключение повторяющихся элементов списка 
a = [1,2,3,4,1,2,3,4]
a = list(set(a))
print(a)

#Добавление элемента
a = {3,13,3,4,15,7}
a.add(9)
a.add(9)
print(a)

a.update([3,14,28]) #Принимает итерабельную послед-ть add(3),add(14),add(28) 
a.update("str")
a.update({1,2,3})
print(a)

#Удаление элементов
a.discard(3)
a.discard(0)
print(a)

a.remove(15)# - remove() выдает ошибку , если удаляемый элемент отсутствует
print(a)

a.pop() # Удаление случайного элемента
print(a)

#a.clear() # Очистить множество

#Операции с множеством
print(len(a))
print("s" in a, 27 in a)
# Пересечение множеств
a = {1,2,3}
b = {4,5,2}
c = {1,7,14}
print(a & b) 
print(a.intersection(b))

# a&=c # Присвоить результат пересечения
# a.intersection_update(b) # Присвоить результат пересечения
print(a)

#Объединение множеств
print(a|b)
print(a.union(b))
print("a - не поменялось",a)

a = a.union(b)
a |=b

#Удаление пересекающихся элементов
print(a-b)

# Все элементы, кроме пересекающихся
print(a^b)

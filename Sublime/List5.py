spisok=[]

for i in range(5):
	a=int(input(""))
	spisok.append(a)
print(spisok)

a=list(range(10))

print(a)

#Добавить в конец списка
print("Добавить в конец списка 7,13")
spisok.append(7) 
spisok.append(13)
print(spisok)
#Добавить в список в нужном месте по индексу
print("Добавить в список 25 на 0-е место и 2-е по индексу")
spisok.insert(0,25)
spisok.insert(2,25)
print(spisok)

#Добавить в список в нужном месте по индексу и распаковать
print("Добавить в список в нужном месте по индексу и распаковать")
spisok.extend([4,5])
print(spisok)
 
#Удалить элемент по индексу  + возвращение удаленного значения
print("Удалить элемент по индексу 2" )
print("Удалить элемент по индексу 0" )
print(spisok.pop(2))
print(spisok.pop(0))
spisok.pop() #Удаление последнего элемента
# pop возвращает удаленное значение
a = spisok.pop()
print(spisok)
print(a)

#Удалить 1-й встречающийся элемент по значению
print("Удалить 1-й встречающийся элемент по значению")
spisok.remove(5)
print(spisok)

#Получить индекс элемента в списке
print("Получить индекс элемента в списке")
print(spisok.index(1))

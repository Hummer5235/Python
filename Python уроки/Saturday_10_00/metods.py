# Методы списков
print('Пример использования метода append')
numbers = [1, 3, 9, 15, 25, 38]

#Добавление в конец списка
numbers.append(100)
print(numbers)

#Удаление элемента по индексу
print('Пример использования метода pop')
numbers.pop(0)
print(numbers)

numbers.pop()
print(numbers)


#-------------------------------------
print('Пример использования метода insert')
names = ['Max','Ivan','Fedor']
print(names)


#Метод insert - добавление элемента на место по индексу
names.insert(0,'Dmitriy')
print(names)

names.insert(2,'Andrey')
print(names)

#------------------------------------------
print('Пример использования метода remove')

fruits = ['Apple', 'Grape', 'Lemon',' Orange']
print(fruits)

# remove - Удаление элемента по значению
fruits.remove('Grape') 
print(fruits)




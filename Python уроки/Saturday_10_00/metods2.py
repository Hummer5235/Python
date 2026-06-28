#Сортировка списка

numbers= [10,3,24,15,57,11]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

#Сортировка слов
names = ['Max', 'Andrey','Phillip','Gleb']
names.sort()
print(names)


#Функция list - создание списка с исп последовательностью
a = list()
print(a)


b = list('Andrey')
print(b)

c = list(range(5))
print(c)

#Метод split - разбивает строку в список. По умолчанию по пробелам
st = 'Hello Andrey, how are you?'
print(st.split())
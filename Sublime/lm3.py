#Удаление по значению
names=["Ivan","Fedor","Alexey"]
names.remove("Fedor")
print(names)

names.remove("Alexey")
print(names)


#Подсчет элементов
#Метод count() - выводит количество элементов с заданным значением
numbers=[1,1,1,3,4,5,2,2,7,4]
print(numbers.count(2))
print(numbers.count(5))
print(f"количество цифр 1 = {numbers.count(1)}шт")

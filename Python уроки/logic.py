#Логические операторы
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

#and - одновременное выполнение всех условий
print(a>b and b>c)

#or - выполнение хотя бы одного из условий
print(a>b or a>c)

#not - отрицание ( противоположное значение)
print(f"not True = {not True} ")
print(f"not a<b = {not a<b}")

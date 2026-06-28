def square(x):
    return x**2

a = list(map(int,input("Введите несколько чисел через пробел: ").split()))
print(a)
b = list(map(square,a))
print(b)

c = list(map(sum,b))
print(c)
# lst = ["Москва","КОСТРОМА","Рязань","КАЛИНИНГРАД"]
#
# d = list(filter(str.isalpha,lst))
# print(d)



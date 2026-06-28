# Функция filter используется для фильтрации элементов итерации (последовательности) с помощью предиката,
# который проверяет каждый элемент на итерации


def odd(x):
    return x%2

lst = [0 ,12 ,4 ,3 ,7 ,5 ,9 ]

c = filter(odd,lst)
print(next(c))
print(next(c))
print(next(c))
print(c)

d = list(filter(lambda x: not x%2, lst))
print(d)
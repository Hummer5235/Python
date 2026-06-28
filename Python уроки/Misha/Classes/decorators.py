#Декораторы - способ расширения возможностей функции , метода, класса извне
from datetime import datetime


# def timeit2(func):
#     start = datetime.now()
#     func()
#     print(datetime.now() - start)


def timeit(func):
    def wrapper(): # Обертка
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def one():
    lst = []
    for i in range(10**7):
        if i %2 == 0:
            lst.append(i)
    return lst

@timeit
def two():
    lst = [i for i in range(10**7) if i%2==0]
    return lst

# lst1 = one()
# lst2 = two()


# timeit2(one)
# timeit2(two)

#Применение функции без декоратора
# one = timeit(one)
# one()
#
# two = timeit(two)
# two()

#С применением декоратора
one()
two()


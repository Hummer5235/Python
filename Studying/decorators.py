#O M
# Декораторы - обертка для функции
from datetime import datetime


def timeit(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def one(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    # time = datetime.now() - start
    # print(time)
    return l

@timeit
def two(n):
    l = [ i for i in range(n) if i %2 ==0 ]
    return l


l1 = one(100)
l2 = two(100)


print(l1)
print(l2)

# def timer(f):
#     start = datetime.now()
#     res = f()
#     time = datetime.now() - start
#     print(time)
#     return res

# timer(one)
# timer(two)


#------------------------------ Пример № 2 --------------------------------------------------------

def upper(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@upper
def greet():
    return "Hello"


def goodbye():
    return 'Goodbye'


ph1 = greet()
ph2 = goodbye()
print(ph1)
print(ph2)




import time

def testTime(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} секунд")
    return wrapper

@testTime # Указывая имя декоратора, мы оборачиваем следующую функцию в декоратор
# Аргументу fn передает ссылку на следующую функцию
def getNOD(a,b):
    while a != b:
        if a>b: a -= b
        else: b -= a
    return a

@testTime
def getFastNOD(a,b):
    if a<b: a,b = b,a
    while b: a,b=b , a%b
    return a



print(getNOD(100000,2))
print(getFastNOD(100000,2))

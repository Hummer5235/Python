import time

def getNOD(a,b):
    while a != b:
        if a>b: a -= b
        else: b -= a
    return a

def getFastNOD(a,b):
    if a<b: a,b = b,a
    while b: a,b=b , a%b
    return a

def testTime(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} секунд")
    return wrapper

test1 =testTime(getNOD)
test2 = testTime(getFastNOD)
print(test1(100000,2))
print(test2(100000,2))


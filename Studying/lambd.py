#Рекурсивная функция - функция которая вызывает сама себя

# lambda arg1,arg2 ...:выражение
r = lambda a,b : a+b
print(r(10,3))

def showElements(lst,func):
    for x in lst:
        if func(x):
            print(x)

def odd(x):
    return True if x%2 != 0 else False

a = [1,4,7,2,4,13,6,8,7]
showElements(a,lambda x: True if x%2 == 0 else False )

a = [1,2,3,4,5,6,7,8,9]
b = list(filter(lambda x: x%2==0,a))
print(b)

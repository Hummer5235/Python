#Использование args
def summa(*args):
    s = 0
    for item in args:
        s += item
    return s

a = summa(1,15,2,7,9)
b = summa(2,4)
print(a)
print(b)










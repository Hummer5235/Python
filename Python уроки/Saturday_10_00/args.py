
a = [10,20,30]
b = (30,31,32)



def summa(*args):
    s = 0
    for i in args:
        s += i
    return s

result = summa(5,1,4,10,4,5)
print(result)

result = summa(13,25,34,16)
print(result)

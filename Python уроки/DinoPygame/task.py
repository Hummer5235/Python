def my_Sum(x,y,*args):
    s = 0
    s += x
    s -= y
    print(args)
    for arg in args:
        s+= arg
    return s

print(my_Sum(10,20,5,6,7,8,9,0))

def myFunc(x,y,*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)


myFunc(1,2,3,10,124,arg5=5,arg17=17)




r = lambda a,b : a+b

n = lambda a,b : a if a>b else b
print(n(50,50))

a = lambda x: True if x%2==0 else False
print(a(10))

p = lambda : "Hello World!"
print(p())

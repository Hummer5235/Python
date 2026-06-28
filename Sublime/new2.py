def func3():
    param = 4
 
    def inner(var):
        var += 1
        return var
 
    param = inner(param)
    return param

print(func3())
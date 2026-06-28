def getValues():
    x = input("x: ")
    y = input("y: ")

    try:
        x = int(x)
        y = int(y)
        return x,y
    except ValueError:
        print("Вы ввели не числовое значение")
        return 0,0

x,y = getValues()
print(x,y)
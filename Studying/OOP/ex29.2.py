
#29. Обработка исключений. Блоки finally и else

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Деление на ноль'



res = 0
try:
    x, y = map(int, input().split())
    res = div(x,y)
except ValueError as z:
    print(z)

print(res)
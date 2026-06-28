
#29. Обработка исключений. Блоки finally и else

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Деление на ноль'



def get_values():
    try:
        x, y = map(int, input().split())
        return x,y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print('Блок finally выполняется до return')

x, y = get_values()
print(x,y)
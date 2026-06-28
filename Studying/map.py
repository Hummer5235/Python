# Функция map применяет указанную функцию к каждому элементу итерируемого объекта
def sq(x):
    return x**2
lst = [1,2,3,-4,-10]
b = map(sq,lst)
b = list(b)
print(b)

# Применение функции len
lst = ["Кострома","Ярославль","Астрахань"]
c = map(len,lst)
c = list(c)
print(c)

# Одно из частых применений функции map
a = list(map(int,input("Введите число: ").split()))
print(a)
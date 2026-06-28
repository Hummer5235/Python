#Функции генераторы
# Необходимы для экономии занимаемой памяти
def f():
    for x in range(10):
        yield x

s = f()  # Генератор
print(s)

print(next(s))
print(next(s))
print(next(s))
print("Конец 1-го задания",end ="\n\n")


#Функция генератор "Среднее арифметическое"
def getAllAverage(N):
    count = 0
    s = 0
    for i in range(1,N+1):
        count += 1
        s += i
        yield s/count

it = getAllAverage(10)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
#Генератор - подвид итерируемых объектов, как список или кортеж
#Для создания генератора в Python внутри функции вместо ключевого слова return используется ключевое слово yield


def counter():
    i = 1
    while i<=10:
        yield i
        i+=1

for i in counter():
    print(i)


def my_gen(x):
    while x > 0:
        if x%2 == 0:
            yield "Even"
        else:
            yield "Odd"
        x-=1

for i in my_gen(7):
    print(i)

print(list(my_gen(5)))


a = [x**2 for x in [1,2,3,4,5,6,7]] #Генераторное выражение для создания списка
b = (x**2 for x in [1,2,3,4,5,6,7]) #Генератор. Используем выражение
print(a)
print(b)
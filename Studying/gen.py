# Генератор
a = [x**2 for x in range(10)]
print(a)
# Итератор
b= (x**2 for x in range(10))
print(b)

it = iter(a)
print(it)
# Перебор элементов итератора при помощи функции next
print(next(it))
print(next(it))

# Отличия списков и генераторов
# lst = list(range(100000000))
lst = (x for x in range(100000000))
for i in lst:
    print(i, end=" ")
    if i >100 :
        break


print("\nnew loop")
for i in lst:
    print(i, end=" ")
    if i > 200 :
        break


print("\n"+str(max(b)))
# Для доступа к элементам по индексу преобразуем в список
print(list(b))
print(b[0])
print(len(b))
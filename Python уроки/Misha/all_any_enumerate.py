#enumerate - возвращает кортеж из индекса элемента и самого элемента
# переданной ей последовательности (итерируемого объекта).

# enumerate(iterable, start) . start - необязательный аргумент

colors = ['red','green','yellow']


for el in enumerate(colors):
    print(el)

print()

for el in enumerate(colors,100):
    print(el)


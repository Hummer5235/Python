names = []
for i in range(5):
    a = input("Введите имя: ")
    names.append(a)

for i in names:
    start = len(names[0])
    if len(i) > start:
        start = i

print(start)
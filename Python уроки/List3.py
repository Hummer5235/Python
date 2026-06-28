numbers = []
for i in range(5):
    a = int(input("Введите число: "))
    numbers.append(a)


smallest_number = numbers[0]
for j in numbers:
    print(j)
    if smallest_number > j:
        smallest_number = j
print(f"Наименьшее число списка: {smallest_number}")



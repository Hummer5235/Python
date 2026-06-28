a = int(input("Введите цену за 1 кг: "))
for i in range(11,22,2):
    n = a * i/10
    print(f"Цена за {i/10} кг равна {n}")


for i in range(1,6):
    n = a * (1+0.2*i)
    print(f"Цена за {1+0.2*i} кг равна {n}")


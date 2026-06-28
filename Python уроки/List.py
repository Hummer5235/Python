numbers = []
counter = 5
for i in range(5):
    print("Осталось ввести чисел: " + str(counter))
    a = int(input("Введите свое число: "))
    counter -= 1
    numbers.append(a)
print(f"Вы составили список чисел: {numbers}")
try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    res = a/b

except ZeroDivisionError as z:
    res = "Ошибка при делении на ноль"
    print(z)
except ValueError as v :
    res = "Вы ввели не число"

else:
    print("Исключений не произошло")

finally:
    print("Блок finally выполняется всегда")

print(res)
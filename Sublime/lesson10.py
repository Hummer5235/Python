
import math

# trunc - отсекает дробную часть
a = float(input("Введите число 1 , функция trunc:"))
a = math.trunc(a)  
print(a)


# floor - округляет до наименьшего целого (3.3 --> 3 , -4.1 --> -5 )
b = float(input("Введите число 2 , функция floor: "))
b = math.floor(b)
print(b)

#ceil - округляет до наибольшего целого (4.2 --> 5 ,  - 0.9 --> 0)
b = float(input("Введите число 3 , функция ceil: "))
b = math.ceil(b)
print(b)
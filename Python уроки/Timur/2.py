# Рассмотрим программу получения цифр двузначного числа:
num = 17
a = num % 10
b = num // 10
print('Первое число',num)
print(a) #Последняя цифра
print(b) #Число дестяков

num = 457
a = num % 10
b =(num % 100) // 10
c =num // 100

print('Второе число',num)
print(a)
print(b)
print(c)

num = 2886
a = num % 10
b =(num % 1000) // 100 // 10
c =num // 1000 // 100
d = num // 1000

print('Третье число',num)
print(a)
print(b)
print(c)



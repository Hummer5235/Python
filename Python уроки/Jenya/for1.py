import random , time
import math

# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#
# print('Было введено', counter, 'чисел, больших 10.')
#
#
# summa = 0
# for _ in range(10):
#     num = int(input())
#     summa += num
#
# print('Сумма чисел: ', summa)
#
# summa = 0
# for _ in range(10,99999):
#     summa += _
#
# print(summa)

#Сигнальная переменная
flag = False

for i in range(100):
    random_number = random.randint(1,100)
    print(random_number)
    if random_number == 33 :
        flag = True

if flag == True :
    print('Я нашел счастливое число!')
else:
    print('К сожалению ничего!')

    




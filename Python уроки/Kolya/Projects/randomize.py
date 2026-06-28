import random # Импортируем модуль
import time



for i in range(0,10):
    num1 = random.randint(1, 100)  # Пишем имя_модуля.название_функции()
    num2 = random.randint(1, 100)  # Пишем имя_модуля.название_функции()
    print(f'№{i}: Случайные числа {num1} и {num2}')
    time.sleep(0.5)



for i in range(10):
    num3 = random.randrange(1, 3) #Аналогична функции range
    print('num3:',num3)

for i in range(10):
    num4 = random.random() #Случайные числа от 0 до 1
    print('num4:',num4)

for i in range(10):
    num5 = round(random.uniform(1.5,2.3),3) #Случайные дробные числа
    print('num5:', num5)
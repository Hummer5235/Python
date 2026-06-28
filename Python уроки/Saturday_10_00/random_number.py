import random

print("Это игра Угадай число! Попробуйте выиграть за  попытки")
n = int(input("Введите число: "))
k = random.randint(1,100)
counter = 1

while n != k:
	n = int(input("Введите число: "))
	counter += 1
	if n >k:
		print("Введите число меньше")
		print()
	else:
		print("Введите число больше")
		print()
		
print(f"'k' было равно:{k}")
print(f"Вы потратили {counter} попытки")

if counter <= 3:
	print("Вы выиграли!")
	
else:
	print("Вы сделали больше 3х попыток:-( и проиграли")
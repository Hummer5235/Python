from random import randint

#Получаем случайное число
k = randint(1,10)
n = int(input("Введите число: "))
s=1

while n!=k:
	print("Неудачная попытка! Повторите снова")
	n = int(input("Введите число: "))
	s+=1
print(f"Удача улыбнулась Вам! Число попыток {s}")


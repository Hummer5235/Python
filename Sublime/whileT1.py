print("Для выхода из программы введите 0 ")
n = int(input("Введите число: "))
s=1
summa=n

while n!=0:
	n = int(input("Введите число: "))
	s+=1
	summa+=n

print(f"Вы ввели {s} чисел")
print(f"Сумма {s} чисел = {summa}")
	
#s = s+1  равно s+=1
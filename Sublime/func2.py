#Функция Сумма
def sum2(a,b):
	return a+b

c=sum2(10,3)
print(f"Сумма чисел {c}")

print(f"Сумма чисел {sum2(12,15)}")

#Функция большее (comparison)
def com(a,b):
	if a>=b:
		return a
	elif b>=a:
		return b

print(f"Ищем большее число {com(3,2)}")

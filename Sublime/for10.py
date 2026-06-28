a = float(input("Цена за кг конфет: "))
s=0
for i in range(2,11,2):
	print(a * (1+i/10))
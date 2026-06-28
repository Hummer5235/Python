import time 

t = int(input("Введите время для таймера: "))

i = 0
while i < t:
	i -= 1
	time.sleep(1)
	print(i)

print("Время закончилось")
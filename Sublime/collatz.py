def collatz(number):
	if number%2 == 0:
		return number//2
	if number%2 == 1:
		return 3*number+1

number=int(input("Введите число: "))
res = collatz(number)
print(res)

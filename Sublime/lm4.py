#Поиск самого частого числа

numbers=[1,2,4,5,5,3,2,2,1,9]

zero=0
for i in numbers:
	if numbers.count(i)> numbers.count(zero):
		zero=i
print(zero)
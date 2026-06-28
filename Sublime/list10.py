numbers = [1,14,20,23,20,20,17,5]
count=len(numbers)

for i in numbers:
	if i == 20:
		numbers.remove(20)
print(numbers)

numbers.reverse()
print(numbers)
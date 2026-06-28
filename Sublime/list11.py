"""Список из ста нулей кроме 1-го и последнего элементов , 
которые должны быть равны 1"""

numbers = []
count = 0
for i in range(100):
	if 0<i<99:
		numbers.append(0)
	else:
		numbers.append(1)
	count+=1
print(count)
print(numbers)
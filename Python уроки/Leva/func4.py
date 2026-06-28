numbers = [10,24, 13, 5]
spisok24 = [1,4,3,2]


def list_append(spisok):
	spisok.pop(-1)
	print(spisok)

list_append(numbers)
list_append(spisok24)
list_append([10,10,10,5000])
list_append(list(range(5)))

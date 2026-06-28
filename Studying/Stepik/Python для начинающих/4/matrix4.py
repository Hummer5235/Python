n = int(input()) # строки
m = int(input()) # столбцы

words =[]


for i in range(n):
	words.append(list())
	for j in range(m):
		el = input()
		words[i].append(el)

for i in range(n):
	for j in range(m):
		print(words[i][j],end=" ")
	print()
tableData = [['apples','oranges','cherries','banana'],
			 ['Alice','Bob','Carol','David'],
			 ['dogs','cats','moose','goose']]


max_length = []

for i in tableData:
	maximum = 0
	for l in i:
		if len(l)>maximum:
			maximum = len(l)
	max_length.append(maximum)
print(max_length)

def printTable():
	for el in range(4):
		for lst in range(3):
			print(tableData[lst][el].rjust(max_length[lst],' '),end=' ')
		print()


printTable()
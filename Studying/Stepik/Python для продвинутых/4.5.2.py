	# put your python code here

	#Максимум в таблице
	n = int(input()) # строки
	m = int(input()) # столбцы



	lst = [input().split() for _ in range(n)]



	maximum = int(lst[0][0])

	maximum_n = 0
	maximum_row = 0

	for i in range(n):
		for j in range(m):
			
			if maximum < int(lst[i][j]):
				maximum = int(lst[i][j])
				maximum_row = i
				maximum_n = j
	print(maximum_row,maximum_n)




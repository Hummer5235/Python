n = 8
matrix = []

for i in range(n):
	matrix.append([0]*n)
	

for i in range(n):
	matrix[i][i] = 1
	matrix[i][n-1-i] = 2

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(6), end='')
    print()



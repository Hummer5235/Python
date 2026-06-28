#След матрицы

n = int(input())
matrix = []

for i in range(n):
	matrix.append(list(map(int,(input().split()))))

summ = 0
for i in range(n):
	summ += matrix[i][i]

print(summ)

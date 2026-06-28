# put your python code here
n = int(input())

matrix = [input().split() for _ in range(n)]

for row in range(len(matrix)):
    for col in range(row):
        matrix[row][col] = matrix[n-row][col]

for row in matrix:
    print(*row)


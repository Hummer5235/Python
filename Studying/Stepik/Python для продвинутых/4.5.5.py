# Обмен диагоналей
n = int(input())
matrix = [input().split() for _ in range(n)]
for row in range(len(matrix)):
    for col in range(row+1):
        if row == col:
            matrix[row][col],matrix[n-row-1][col] = matrix[n-row-1][col],matrix[row][col]
        
        
for i in matrix:
    print(*i)
        


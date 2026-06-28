#Поворот матрицы на 90гр
n = int(input())
matrix = [input().split() for _ in range(n)] 
new_matrix = [[] for i in range(n)]
for row in range(n):
    for col in range(n):
        new_matrix[row].append(matrix[n-col-1][row])
        

for row in new_matrix:
    print(*row)




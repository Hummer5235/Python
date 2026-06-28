#Максимальный элемент ниже главной диагонали
n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

max = matrix[0][0]
for i in range(len(matrix)):
    for j in range(i+1):
        if j <= i:
            if matrix[i][j] > max:
                max = matrix[i][j]

print(max)

# Второй вариант
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
max_numbers = []
for i in range(n):
    max_numbers.append(max(matrix[i][:i + 1]))

print(max(max_numbers))

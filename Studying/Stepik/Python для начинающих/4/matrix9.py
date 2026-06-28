#Максимальный элемент левой и правой четверти
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

max = matrix[0][0]
for i in range(len(matrix)):
    for j in range(n):
        if j <= i and i <= n - 1 -j or j >= i and i >= n - 1 - j :
            if matrix[i][j] > max:
                max = matrix[i][j]

print(max)

#Второй вариант
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

maximum = []
print(max([matrix[i][j] for i in range(n) for j in range(n) if j <= i and i <= n - 1 -j or j >= i and i >= n - 1 - j ]))





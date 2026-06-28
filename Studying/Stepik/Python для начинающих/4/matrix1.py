#Главная диагональ
i = j
#Побочная диагональ
n = i + j + 1
j = n - i - 1

rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()


# print("32".ljust(3,'*'))
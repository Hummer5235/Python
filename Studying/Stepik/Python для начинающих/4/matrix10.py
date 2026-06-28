# Сумма элементов по четвертям
# Элементы диагоналей не учитываются
matrix = []
n = int(input())
for i in range(n):
    matrix.append(list(map(int,input().split())))

summa_up = 0
summa_rt = 0
summa_dw = 0
summa_lt = 0



for i in range(len(matrix)):
    for j in range(n):
        if j > i and i < n - 1 -j:
            
            summa_up += matrix[i][j]
        

        if j > i and i > n - 1 - j:
            summa_rt += matrix[i][j]
        
        
        if j < i and i > n - 1 - j:
            summa_dw += matrix[i][j]
        
        
        if j < i and i < n - 1 - j:
            summa_lt += matrix[i][j]
        
        

print(f"Верхняя четверть: {summa_up}")
print(f"Правая четверть: {summa_rt}")
print(f"Нижняя четверть: {summa_dw}")
print(f"Левая четверть: {summa_lt}")

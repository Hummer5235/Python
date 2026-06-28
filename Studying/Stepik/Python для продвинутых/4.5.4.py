# put your python code here
# Симметричная матрица
n = int(input())
matrix = [input().split() for i in range(n)]
result = 'YES'

for row in range(len(matrix)):
    for col in range(row):
        if row != col:
            if matrix[row][col] !=matrix[col][row]:
                result = 'NO'
                break
    if result == 'NO':
        break
print(result)

                
                



            
                








#Магический квадрат
n = int(input())
matrix = [input().split() for i in range(n)]
lst =  [i**2 for i in range(1,n+1)]
result = 'YES'


#Превращение в целые числа
for i in range(n):
    for g in range(n):
        matrix[i][g] = int(matrix[i][g])


sum_of_rows = sum(matrix[0])
sum_of_cols =0
sum_of_main_diag = 0
sum_of_sec_diag = 0

        
for i in range(n):
    sum_of_main_diag += matrix[i][i]
    sum_of_sec_diag += matrix[n-i-1][i]
    if sum(matrix[i])!= sum_of_rows:
        result = 'NO'
        break
    for g in range(n):
        sum_of_cols += matrix[g][i]
    if sum_of_cols!= sum_of_rows:
        result = 'NO'
        break
    sum_of_cols =0           
if  sum_of_main_diag != sum_of_rows or sum_of_sec_diag != sum_of_rows :
    result = 'NO'

new_lst = []    
for i in matrix:
    new_lst += i
if result == 'YES':
    for i in lst:
        if i not in new_lst:
            result = 'NO'
            break
    

print(result)
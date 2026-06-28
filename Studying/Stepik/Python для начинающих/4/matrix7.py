n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

counter = 0
for i in matrix:
    middle = sum(i)/n
    for j in i:
        if j > middle:
            counter +=1
    print(counter)
    counter = 0



# Хорошее решение
#list comprehension и генераторы
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst) / len(lst)
    print(sum(i > avg for i in lst))

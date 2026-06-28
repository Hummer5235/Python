import math
lst = input().split()
n = int(input())

new_lst = []

if n > 1:

    for i in range(math.ceil(len(lst)/2)):
        if len(lst[:n]) > 0:
            new_lst.append(lst[:n])
        del lst[:n]

else:
    new_lst = [[i] for i in lst]


print(new_lst)
    
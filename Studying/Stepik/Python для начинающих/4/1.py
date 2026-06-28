# n , m = int(input()), int(input())
# my_list = []

# for i in range(n):
# 	my_list.append([0]*m)

# print(my_list)

#--------------------

# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n

# for i in range(n):
#     my_list[i] = [0] * m

# print(my_list)



#------------------

# n, m = int(input()), int(input())    # считываем значения n и m

# my_list = [[0] * m for _ in range(n)]

# print(my_list)

#--------------------
# Не создают список умножая список на число
n, m = int(input()), int(input())    # считываем значения n и m

my_list = [[0] * m ] * n

print(my_list)

my_list[0][0] = 17
print(my_list)
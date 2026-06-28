num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')




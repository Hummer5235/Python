n = int(input())

res = 0
f_total = 0
while True:
    while n>0:
        f_total+= n%10 # 2 + 9 + 1 = 12 
        n //= 10
    if f_total <=9:
        break
    else:
        n = f_total
        f_total = 0
print(f_total)
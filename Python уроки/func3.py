def sum_range(start,end):
    sum = 0
    for i in range(start,end+1):
        sum+=i

    return sum
list=[0,4,10,13,-4,2,5]
print(sum_range(0,3))
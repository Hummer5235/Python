
list = [1,2,2,3,5,8,2,1,1,9,9]

counter = 0
for i in list:
    if list.count(i) > 1:
        counter += list.count(i)
        for j in range(list.count(i)):
            list.remove(i)
        print(list)
print(counter)


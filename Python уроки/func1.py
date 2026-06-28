def max_element(list):
    max = list[0]
    for i in list:
        if i>max:
            max = i
    return max

list=[0,4,10,13,-4,2,5]
print(max_element(list))
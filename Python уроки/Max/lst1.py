a = [1,2,2,3,3,4,5,5,5,5,5,6,7,8,9]
b = [2,3,5,11,6]
c = []
def merge(lst1,lst2):
    for el in lst1:
        if el in lst2 and el not in c:
            c.append(el)

merge(a,b)

print(c)

from functools import reduce
with open('nums.txt') as file:
    content = list(file.read())
    summa = 0
    st=''
    for i in content:
        if i.isdigit():
            st = st+i
            
        elif st!='':
            summa+=int(st)   
            st = ''
    print(summa)
    






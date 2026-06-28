with open('population.txt') as file:
    file = map(str.strip,file.readlines())
    for line in file:
        temp_lst = line.split()
        if temp_lst[0][0]=='G' and int(temp_lst[-1])>500000:
            print(*temp_lst[:-1])




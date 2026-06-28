with open(input()) as file:
    temp_lst = []
    for line in file:
        temp_lst.append(line.strip())
        if len(temp_lst) > 10:
            del temp_lst[0]
    print(*temp_lst,sep ='\n')





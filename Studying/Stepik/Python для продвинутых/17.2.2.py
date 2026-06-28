with open('data.txt') as file:
    print(*file.readlines()[::-1],sep ='')
    



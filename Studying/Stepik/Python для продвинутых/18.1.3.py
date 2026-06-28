with open('grades.txt') as file:
    res = list(map(lambda line: int(line.split()[1])>=65 and int(line.split()[2])>=65 and int(line.split()[3])>=65,file.readlines()))
    res = list(filter(lambda x: x ==True, res))
    print(len(res))




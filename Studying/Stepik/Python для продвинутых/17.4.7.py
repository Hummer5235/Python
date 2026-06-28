# put your python code here
with open('logfile.txt',encoding='utf-8') as file1, open('output.txt','w',encoding='utf-8') as out:
    lines = []
    res = []
    for line in file1:
        line = list(map(lambda x: x.strip(), line.split(',')))
        lines.append(line)
    for line in lines:
        el1 = float(line[1].replace(':','.'))
        el2 = float(line[2].replace(':','.'))
        if el2-el1 >= 1:
            out.write(line[0]+'\n')

            



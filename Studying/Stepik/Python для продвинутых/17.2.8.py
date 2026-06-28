
def read_csv():
    finally_lst = []
    with open('data.csv') as file:
        lst = list(map(str.strip,file.readline().split(',')))
        for line in file.readlines():
            line_lst = line.strip().split(',')
            dictionary = {}
            for i in range(len(lst)):
                dictionary[lst[i]] =line_lst[i]
            finally_lst.append(dictionary)
        return finally_lst




print(read_csv())

with open('lines.txt') as file:
    content_list = file.readlines()
    content_list = list(map(str.strip,content_list))
    len_max_el = len(max(content_list,key = lambda x: len(x)))
    for i in content_list:
        if len(i) == len_max_el:
            print(i)


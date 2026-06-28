# with open('goats.txt') as file1, open('answer.txt','w') as file2:
#     list_of_colors = []
#     list_of_goats = []
#     for line in file1:
#         if line =="GOATS\n":
#             break
#         elif line != 'COLOURS\n':
#             list_of_colors.append(line)
#     for line in file1:
#         list_of_goats.append(line)
#     print(list_of_colors)
#     print(list_of_goats)

#     content = file1.readlines()
#     temp_lst = []
#     for i in list_of_goats:
#         print(i, list_of_goats.count(i)/len(list_of_goats))
#         if list_of_goats.count(i)/len(list_of_goats) > 0.07:
#             if i not in temp_lst:
#                     temp_lst.append(i)
#     temp_lst.sort()
#     print(temp_lst)
#     for line in temp_lst:
#         file2.write(line)
    

# put your python code here
with open('goats.txt') as file1, open('answer.txt','w') as file2:
    content = file1.read().split('\n')
    colors = content[1:content.index('GOATS')]
    goats = content[content.index('GOATS')+1:]
    res = list(filter(lambda x: goats.count(x)/len(goats) > 0.07 , colors))
    res.sort()
    for line in res:
        file2.write(line+'\n')
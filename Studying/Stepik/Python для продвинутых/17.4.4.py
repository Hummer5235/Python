
with open('class_scores.txt') as file1 , open('new_scores.txt','w') as file2:
    for line in file1:
        lst_from_string = line.split()
        file2.write(f'{lst_from_string [0]} ')
        if int(lst_from_string [1])+5 < 100:
            file2.write(f'{str(int(lst_from_string [1])+5)}\n')
        else:
            file2.write(f'100 \n')



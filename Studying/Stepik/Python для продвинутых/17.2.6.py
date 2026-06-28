with open('file.txt') as file:
    words =0
    lines = 0
    letters = 0
    for line in file:
        lines += 1
        words += len(line.split())
        for letter in line:
            if letter.isalpha():
                letters += 1
    print('Input file contains:')
    print(letters,'letters')
    print(words,'words')
    print(lines,'lines')
   





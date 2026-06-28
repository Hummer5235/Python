with open(input()) as file, open('forbidden_words.txt') as words:
    list_of_words = words.read().lower().split()
    list_of_words = list(map(str.strip,list_of_words))
    for line in file:
        for word in list_of_words:
            while line.lower().count(word)>0:
                line = line[:line.lower().index(word)]+'*'*len(word)+line[line.lower().index(word)+len(word):]
        print(line.strip())





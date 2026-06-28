with open('words.txt') as file:
    content = file.read().split()
    max_length = len(max(content,key=len))
    res = [word for word in content if len(word)==max_length]
    print(*res,sep='\n')
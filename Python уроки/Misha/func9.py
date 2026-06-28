lst = ['python','level','samsung','cat','everybody','paap']

more_six = list(filter(lambda word: len(word)>=6,lst))
e_in_word = list(filter(lambda word: 'e' in word ,lst))
palindrom = list(filter(lambda word: word==word[::-1] ,lst))
print(more_six)
print(e_in_word)
print(palindrom)


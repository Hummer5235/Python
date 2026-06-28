# объявление функции
def is_pangram(text):
    alph =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lst = []
    for i in alph:
        if i in text.lower() and i not in lst:
            lst.append(i)
    if len(lst) == 26:
        print(lst,len(lst))
        return True
    else:
        print(lst,len(lst))
        return False

    

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
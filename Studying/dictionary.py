

dict = {"Hello":"Привет","Goodbye":"До свидания"}

def add(key,value):
    dict.update({key:value})

def delete(word):
    del dict[word]

def show():
    print(dict)





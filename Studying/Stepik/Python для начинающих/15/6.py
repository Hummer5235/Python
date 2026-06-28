
#Шифр Цезаря. Сдвиг в зависимости от длины слова
simbols = ',."!'

eng_language = 'abcdefghijklmnopqrstuvwxyz'
rus_language = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

languages = [eng_language,rus_language]

st_res = ''
st = input()


language = languages[0]
step = 26
st_new=st
for i in simbols:
    st_new=st_new.replace(i,'')
list_of_lens = [len(i) for i in st_new.split()]

counter = 0
for i in st :
    if i.isalpha():
        if language.index(i.lower()) + list_of_lens[counter]> len(language)-1:
            if i.isupper():
                st_res += language[language.index(i.lower())-step+list_of_lens[counter]].upper()
            else:
                st_res += language[language.index(i)-step+list_of_lens[counter]]
            counter +=1
        else:
            if i.isupper():
                st_res += language[language.index(i.lower())+list_of_lens[counter]].upper()
            else:
                st_res += language[language.index(i)+list_of_lens[counter]]

    else:
        st_res += i
    


print(st_res,list_of_lens)





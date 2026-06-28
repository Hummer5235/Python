length = int(input('Введите высоту елки: '))

for i in range(length):
    if i != length-1:
        print(' '*(length-i)+'/'+' '*i*2+'\\')
    else:
        print(' '*(length-i)+'/'+'_'*(length * 2-2)+'\\')
print(' '*length+'||')


A = int(input('Введите число: '))
B = int(input('Введите число: '))
C = int(input('Введите число: '))

#and - логическое "И". Все условия должны быть True 
print('A самое большое число:' , A>B and A>C)
print('True and True: ',True and True)
print('True and False: ',True and False)
print('False and False: ',False and False)

print()
#or - логическое "ИЛИ". Достаточно одно из условий
print('True or True: ',True or True)
print('True or False: ',True or False)
print('False or False: ',False or False)

print()
#not - логическое "НЕ"
print(not True)
print(not False)


print(not 1==0)




a = 0
b = 5
c = 10

print(f'Переменная а больше чем b и c {a>b and a>c}') # True and False


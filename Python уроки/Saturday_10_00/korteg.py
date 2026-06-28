#tuple - Кортеж
eggs = ('hello', 12, 0.1)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
#eggs[0] = 100

a = ('hello')
b = ('hello',)
print(type(eggs))
print(type(a))
print(type(b))


#list - функция превращения в список
#tuple - функция превращения в кортеж
eggs2 = list(eggs)
print(eggs,eggs2)

eggs3 = tuple([1,2,3,4,5])
print(eggs3)
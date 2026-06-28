#Словарь - коллекция многих значенией, словарь не упорядочен
#Ключ
#Значение
myCat = {'size':'fat','color':'orange'}  # Словарь myCat

# Ключи - 'size' , 'color'
# Значения - 'fat','orange'

print(myCat['size'])

print(f"My cat has {myCat['color']} color ")


test_dict = {1:"Sonya", 2:"Andrey"}
print(test_dict[1],test_dict[2])

#Сравнение словарей и списков
animals1 = ['cat','dog']
animals2= ['dog','cat']
print(animals1 == animals2)

names = {'name1':'Sonya','name2':'Andrey'}
names2 = {'name2':'Andrey','name1':'Sonya'}
print(names == names2)
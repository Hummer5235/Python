import pickle

file = open('file7.bin','wb+',encoding='binary')
lst = ['Яблоко','Апельсин']
pickle.dump(lst,file)

file = open('file7.bin','rb')



# fruits = pickle.load(file)
# file.seek(0)
print(fruits)

for i in range(3):
	a = input('Введите название фрукта: ')
	fruits.append(a)

# file = open('file7.bin','wb')
# pickle.dump(fruits,file)
print(fruits)	
file.close()

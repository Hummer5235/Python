N=int(input("Введите количество чисел: "))
strings=[]
for i in range(N):
	strings.append(input("Строку: "))
print(strings)

count=0
for i in strings:
	if i.count("o")==2:
		count+=1
print(count)

N=int(input("Введите количество чисел: "))
strings=[]
for i in range(N):
	strings.append(input("Строку: "))
print(strings)

l=0
word=0
for i in strings:
	if len(i)>=l:
		word=i
		l=len(i)
print(word)
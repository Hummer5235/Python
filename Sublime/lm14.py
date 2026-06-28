N=int(input("Введите количество чисел: "))
strings=[]
for i in range(N):
	strings.append(input("Введите число: "))
print(strings)

for idx in range(len(strings)):
	strings[idx]=int(strings[idx])
print(strings)

l=0


for i in strings:
	if strings.count(i)>l:
		l=i
print(l)

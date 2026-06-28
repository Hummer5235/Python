#Ссылки
# spam=[0,1,2,3,4,5]
# cheese = spam
# cheese[1]="Hello!"
# print(spam)

#Вложенные списки
a = [[0,1,2,1],
	 [2,4,1,9],
	 [71,13,1,25]]
print(len(a))

print(a[2])
print(a[2][1])
b=["hello","world"]
print(b[1][1])

#Сумма элементов вложенного списка
for i in range(3):
	sum=0
	for j in range(4):
		print(a[i][j],end=" ")
		sum+=a[i][j]	
	print(sum)

#Заполнение вложенного списка
a=[]
n = int(input()) #Stroka
m = int(input()) #Stolb

for i in range(n):
	b=[]
	for i in range(m):	
		b.append([1]*3)
	a.append(b)
 
for i in a:
	print(i)


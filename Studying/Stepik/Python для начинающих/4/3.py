n = int(input())
lst = []
lst_time =[]
for i in range(n):
	for j in range(1,n+1):
		lst_time.append(j)
	lst.append(lst_time)
	lst_time = []

for i in lst:
	print(i)

#----------------
n = int(input())
lst = []
for i in range(n):
	lst.append(list(range(1,n+1)))

for i in lst:
	print(i)
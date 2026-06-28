string = input().split()
lst = list(map(int,string))
lst_new = []
lst_new.append(lst[-1])
for i in range(len(lst)-1):
	lst_new.append(i) 



for i in lst_new:
	print(i,end=" ")
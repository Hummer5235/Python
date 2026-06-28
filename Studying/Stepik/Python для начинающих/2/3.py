string = input().split()
lst = list(map(int,string))

for i in range(0,len(lst),2):
	if i+1 < len(lst):
		lst[i],lst[i+1] = lst[i+1],lst[i]
	

for i in lst:
	print(i,end=" ")
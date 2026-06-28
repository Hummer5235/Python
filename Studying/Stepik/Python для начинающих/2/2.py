lst = list(map(int,input().split()))
print(lst)
count = 0
for idx in range(len(lst)):
	if idx != 0:
		if lst[idx] > lst[idx-1]:
			count += 1
print(count)
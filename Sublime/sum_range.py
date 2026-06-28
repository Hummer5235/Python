
def sum_range(start,end):
	total=0
	if start < end:
		for i in range(start,end+1):
			total+=i
	else:
		for i in range(end,start+1):
			total+=i

	print(total)

sum_range(7,3)
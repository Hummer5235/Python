def useless(s):
	for i in range(len(s)-1):
		if s[i] < s[i+1]:
			m=s[i+1]
	res=m/len(s)
	return res
print(useless([1,4,2,7,15,3,9,16]))

z = ['a', 'b', 'a', 'c', 'b', 'a', ]
x=[]


for i in range(len(z)):
	print(i)
	print(z)
	if i == z.index(z[i]):
		print(i)
		x.append(z[i])
print(x)
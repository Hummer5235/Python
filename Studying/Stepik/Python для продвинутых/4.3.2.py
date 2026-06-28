st = input()
lst_from_st = st.split()
lst = [[]]
print(lst_from_st)

for i in lst_from_st:
	lst.append([i])


for i in range(len(lst_from_st)):
	for j in range(len(lst_from_st)):
		if len(lst_from_st[i:i+j]) > 1 and j>= i:
			lst.append(lst_from_st[i:i+j])
			print(lst_from_st[i:i+j],i,j)

if len(lst_from_st)>1:
	lst.append(lst_from_st)

print(lst)
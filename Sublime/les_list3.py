# spisok = []
# for i in range(5):
# 	spisok.append(input())
# print(spisok)

spisok2 = []
N = int(input())
for i in range (N):
	a2 = int(input())
	spisok2.append(a2)
print(spisok2)
spisok2.sort()
print(spisok2[-1])

for i in spisok2:
	if i<10:
		print(i)
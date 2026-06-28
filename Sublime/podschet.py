#Метод подсчета. Сортировка подсчетом Python
# Задание_3
# a = [1,2,5,2,1,3,4,1,1,2,3,1,3,4,5,4,3]
# count = [0]*6
# for i in a:
#  	count[i]+=1
# print(count)

# for i in range(6):
# 	if count[i]>0:
# 		for j in range(count[i]):

# 			print(i,end ="")
# 	print()

# # Задание_2

# s = "hjadksadk DFSASD asdxzv z&^#@( ,y zo pk ll b)))"
# letters = [0]*26
# for i in s.lower():
# 	if "z">=i>="a": 
# 		number = ord(i) - 97
# 		letters[number]+=1

# for i in range(26):
# 	if letters[i]>0:
# 		print(str(letters[i])+chr(i+97),end=" ")
 
# Задание_3

a = []
import random

for i in range(10):
	a.append(random.randint(-10,10))
print(a)

count = [0]*21

for i in a:
	count[i+10]+=1
for i in range(21):
	if count[i]>0:
		print(i-10,count[i])


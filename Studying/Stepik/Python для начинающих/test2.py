# put your python code here

s = input()
counter = 0
for i in range(len(s)//2):
    if s[i]==s[-i-1]:
        counter +=1
if counter == len(s)//2:
    print('YES')
else:
    print('NO')




print(counter,len(s)//2)


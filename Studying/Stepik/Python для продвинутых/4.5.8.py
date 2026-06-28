# put your python code here
n = input()
chess_alph = ['a','b','c','d','e','f','g','h']
lst = [ ['.','.','.','.','.','.','.','.'] for i in range(8) ]
y1 = 8-int(n[1])
x1 = chess_alph.index(n[0])
print(x1,y1)
lst[y1][x1] = 'N'



for x in range(8):
    for y in range(8):
        if (abs(x-x1)==1 and abs(y-y1) == 2) or (abs(x-x1)==2 and abs(y-y1)==1):
            print(y,x)
            lst[y][x] = '*'

for i in lst:
    print(*i)




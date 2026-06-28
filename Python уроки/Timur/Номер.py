n = input()
x = n.split('-')
s = 0
for i in range(len(x)):
    for j in x[i]:
        if j in '0123456789':
            if i > 3:
                break
            if len(x) == 3:
                if len(x[0]) == 3:
                    s += 1
                if len(x[1]) == 3:
                    s += 1
                if len(x[2]) == 4:
                    s += 1
            if len(x) == 4:
                if len(x[0]) == 1:
                    if x[0] == '7':
                        s += 1
                if len(x[1]) == 3:
                    s += 1
                if len(x[2]) == 3:
                    s += 1
                if len(x[3]) == 4:
                    s += 1

if len(x) == 4:
    if s == (len(n) - 3) * len(x):
        print('YES')
    else:
        print('NO')
elif len(x) == 3:
    if s == (len(n) - 2) * len(x):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
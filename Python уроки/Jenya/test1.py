a = [17, 24, 91, 96, 67, -27, 79, -71, -71]

n = len(a)

flag = False
for i in range(n - 1):
    for j in range(n - i - 1):
        print(a[i],a[j])
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
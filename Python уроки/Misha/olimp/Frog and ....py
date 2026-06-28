
import time


N = int(input())
start = time.time()
road = N
count = 0
while road > 3:
    road = road - 1
    if road - 3 == 0 or road - 3 >3:
        road = road - 3
    elif road - 2 == 0:
        road= road-2
    else:
        road = road -3
    count+=1
end = time.time() - start
print(f'road:{road}', f'count:{count}',f'time:{end}' )


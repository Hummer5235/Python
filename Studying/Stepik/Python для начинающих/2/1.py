strings = int(input())
first = 0
second = 0
third = 0
fourth = 0

for i in range(strings):
	x, y = map(int,input().split())
	if x < 0 and y > 0 :
		second += 1
	elif x > 0 and y > 0 :
		first += 1
	elif x < 0 and y < 0 :
		third += 1
	elif x > 0 and y < 0 :
		fourth += 1
print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")



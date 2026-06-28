

# x*10+y*5+z*0.5 == 100


for x in range(100):
	for y in range(100):
		for z in range(100):
			if x*10+y*5+z*0.5 == 100 and x+y+z == 100:
				print(f'x={x},y={y},z={z}')
# x,y - координаты
# w - ширина , h - высота 
# px,py - координаты точки
x = int(input("Введите x: "))
y = int(input("Введите y: "))
w = int(input("Введите w: "))
h = int(input("Введите h: "))

px = int(input("Введите px: "))
py =int(input("Введите py: "))

if (x <= px <= x+w) and (y <= py <= y+h):
	print("Да, точка внутри прямоугольника")
else:
	print("Точка не в прямоугольнике")
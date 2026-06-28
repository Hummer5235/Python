
# class Geom:
# 	pass


#object - Базовый класс, от которого наследуется любой созданный нами класс
#Это сделано для работы по единому образцу
#object - предок всех классов




class Geom:
	pass
	
class Line(Geom):
	pass

class Formula:
	pass

a = object() # Создаем напрямую от класса object

print(Geom)
g = Geom()

line = Line()
print(line.__class__)



print('адрес объекта', g)
print('адрес объекта', a)


print('Line подкласс Geom?',issubclass(Line,Geom))
print('Geom подкласс object?',issubclass(Geom,object))
print('Line подкласс object?',issubclass(Line,object))
print('Line подкласс Formula?',issubclass(Line,Formula))





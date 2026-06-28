#Площадь треугольника (Формула Герона)
import math

def are_tri(a,b,c):
	p=(a+b+c)/2
	S=math.sqrt(p*(p-a)*(p-b)*(p-c))
	return S

print(are_tri(3,4,5))

#Площадь круга

def are_cir(R):
	P=3.14
	S=P*R**2
	return S
print(are_cir(5))
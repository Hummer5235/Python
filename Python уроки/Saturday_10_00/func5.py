def p_s (a,b):
	P = (a+b)*2
	S = a*b
	return P, S
	print('После команды return ничего не выполняется') 


P, S = p_s(10,5)
print(f'Периметр {P}, Площадь {S}')

P, S = p_s(90,7)
print(f'Периметр {P}, Площадь {S}')
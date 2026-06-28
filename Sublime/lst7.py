numbers = [1,2,10,17,4,93]

#Смена 1 и последнего элементов местами
def change_lst(list):
	a = list.pop(0)
	b = list.pop()
	list.append(a)
	list.insert(0,b)
	return list
print(change_lst(numbers))	

#Смена 1 и последнего элементов местами

def change(lst):
	lst[-1],lst[0]=lst[0],lst[-1]
	return lst

print(change([1,2,3,13,7]))

"""Переменная args, обозначающая неограниченное количество 
неименованных параметров, представлена внутри любой 
функции в виде кортежа. Если применить к нему функцию list(), 
то получим требуемый список."""
def to_list(*args):
    return list(args)

print(to_list(1,2,3))
print(to_list("Кофе",2,"с молоком"))

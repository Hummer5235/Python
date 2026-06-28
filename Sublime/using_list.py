# Это мой список покупок  
shoplist = []
N = int(input("Введите кол-во покупок: "))
for i in range(N):
	a = input("Введите продукт: ")
	shoplist.append(a)

print("\nЯ должен сделать",len(shoplist), "покупки")

print("\nПокупки:", end = " ")

for item in shoplist:
	print(item,end=" ")


print(f"\nТакже нужно купить риса.")
shoplist.append("рис")

print("\nТеперь мой список покупок выглядит так: ")
print(shoplist)


print("Первое, что мне нужно купить, это", shoplist[0])
print("Я купил: ",shoplist.pop(0))


print("\nТеперь мой список покупок выглядит так: ")
print(shoplist)

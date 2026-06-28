lst = input("Напишите города где вы были через запятую: ").replace(" ","").split(",")
print(lst)

b = list(filter(str.isalpha,lst))
print(b)
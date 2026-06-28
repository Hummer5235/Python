# spam={"color":"red","age":"37"}

# #Итерации по значениям
# for v in spam.values():
# 	print(v,end=" ")
# print()
# #Итерации по ключам
# for k in spam.keys():
# 	print(k,end=" ")
# print()
# #Итерации по парам "ключ-значение"
# for i in spam.items():
# 	print(i,end=" ")
# print()

# print(spam.keys())
# print(list(spam.items()))
# #Типы данных
# print(spam.keys())
# print(spam.values())
# print(spam.items())


# #Групповое присваивание
# for k,v in spam.items():
# 	print("Key: "+ k + " Value: "+str(v))


#Метод get()
picnicItems={"apples":5,"cups":2}
print("I m bringing "+str(picnicItems.get("cups",0))+" cups")
print("I m bringing "+str(picnicItems.get("eggs",0))+" eggs")

#Метод setdefault()
picnicItems.setdefault("color","black")
print(picnicItems)
print(picnicItems["color"])
print(picnicItems)
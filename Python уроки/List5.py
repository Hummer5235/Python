list1 = ["mango","apple","watermelon","grapes","orange","lemon","kiwi"]
list2=["banana","watermelon","orange","kiwi","mango"]
list3=[]

for i in list1:
    if i in list2:
        list3.append(i)
print(f"Список общих фруктов: {list3}")


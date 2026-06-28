# #Метод get()
# picnicItems={"apples":5,"cups":2}
# print("I m bringing "+str(picnicItems.get("cups",0))+" cups")
# print("I m bringing "+str(picnicItems.get("eggs",0))+" eggs")

# #Метод setdefault()
# picnicItems.setdefault("color","black")
# print(picnicItems)
# print(picnicItems["color"])
# print(picnicItems)

message="It was a bright cold day in April, and the clocks were striking thirteen"
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1
print(count)

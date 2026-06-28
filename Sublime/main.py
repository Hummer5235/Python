import os

# file = open("readme.txt","w")
# file.write("Surprise")
# file.close()

# file = open("readme.txt")

# data = file.read()
# print(data)
# file.close()

pic = "road.jpg"
file = open(pic,"rb")

new_file = open("copy"+pic, "wb")
new_file.write(file.read())
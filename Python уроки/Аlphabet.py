letters = "фаАЫПФччмАДчУусовЩорРноК"
clean_string=""
for i in letters:
    if i.islower():
        clean_string+=i
letters = clean_string
print(letters)
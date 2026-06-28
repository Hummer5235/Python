# Фильтрация


#(values) = [(expression) for (value) in (collection) if (condition)]


names = ["john","jack","max","harald"]

new_names = [n for n in names if n[0]=="j"]
print(new_names)


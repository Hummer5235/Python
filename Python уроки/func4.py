def reverse_str(str):
    str_new = ""
    i = 0
    index = len(str)
    while index > 0 :
        str_new += str[index-1]
        index -= 1
    return str_new

print(reverse_str("mixaM"))

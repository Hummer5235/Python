string = input()
length = len(string)
res = length * 60
print(f"{round(res//100)} р. {res%100} коп." )

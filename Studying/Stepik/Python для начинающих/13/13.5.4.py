# объявление функции
def is_valid_password(password):
    lst = [i for i in range(len(password)) if password[i]==':']
    lst.append(-1)
    if len(lst)>3:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    num1 = password[:lst[0]]
    num2 = int(password[lst[0]+1:lst[1]])
    num3 = int(password[lst[1]+1:])
    
    if num1==num1[::-1]:
        flag1 = True
         
    counter = 0
    for i in range(2,num2+1):
        if num2 % i == 0:
            counter += 1
    if counter == 1:
        flag2 = True
    
    if num3 %2 == 0:
        flag3 = True
    
    if flag1 and flag2 and flag3:
        return True
    return False
    

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
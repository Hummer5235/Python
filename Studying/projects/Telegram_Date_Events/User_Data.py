

def append_user(user,count):
    with open('users_list.txt','a') as file:
        file.write(f'{str(user)},')
def read_users():
    with open('users_list.txt','r') as file:
        list = file.read().split(',')
        list = [int(i) for i in list if i.isdecimal()]
    return list
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    if password == password.upper():
        return False
    if password == password.lower():
        return False
    if len([i for i in password if i in '1234567890']) == 0:
        return False
    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
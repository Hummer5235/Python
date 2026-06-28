# model = int(input())

while model != 100 or model != 200 or model != 300:
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())







def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False


model = int(input())
while  is_invalid(model):
    model = int(input())
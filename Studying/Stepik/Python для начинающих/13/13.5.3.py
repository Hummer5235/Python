# объявление функции
def is_palindrome(text):
    for i in ' ,.!?-':
        text = text.replace(i,'')
    half = len(text)//2
    print(len(text))
    print(len(text[:half]),len(text[:half:-1]))
    print(text[:half],text[:half:-1])
    if text[:half]==text[:half:-1]:
        return True

    return False
# считываем данные
txt = input().lower()

# вызываем функцию
print(is_palindrome(txt))
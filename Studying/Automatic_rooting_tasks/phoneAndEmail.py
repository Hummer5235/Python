#Нахождение телефонов и email адресов

import re, pyperclip


text = str(pyperclip.paste())
match = re.findall(r'(\+\d)?\s?\(?\d{3}\)?\W*\d{3}\W*\d{4}',text)
print(match)


match2 = re.findall(r'\w+@\w+[.]com',text)
print(match2)


lst = []
print('Найденные контакты:')
lst += match
lst += match2
result = '\n'.join(lst)
print(result)
pyperclip.copy(result)
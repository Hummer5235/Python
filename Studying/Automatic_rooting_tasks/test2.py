import re

# line = re.compile('.*',re.DOTALL)
# match = line.search('Server is not \n avaluable')
# print(match.group())


#Игнорирование регистра. Указание флага re.IGNORECASE

# text = 'МонотОнный ТОНЕТ в тине'
# match = re.findall('тон',text,re.I)
# print(match)


numbers = '42 1,234 6,365,731 12,34,567 1234 345'
a = re.findall(r'(?<!,)\b\d{1,3}\b(?!,)|(?<!,)\b\d{1,3}\b(?:,\d{3})*',numbers)
print(a)


names = 'satoshi Nakamoto Satoshi Nakamoto Mr. Nakamoto Alice Nakamoto Nakamoto Satoshi nakamoto RoboCop Nakamoto '

res = re.findall(r'[A-Z]+\w*\s*Nakamoto',names)
print(res)


stories = 'RoboCop eats apples. Alice THROWS FOOTBALLS. Alice eats apples. Bob pets cats. Carol throws baseballs. Carol eats 7 cats. Alice throws Apples. BOB EATS CATS.'

res = re.findall(r'(?:Bob|Carol|Alice)\s(?:eats|pets|throws)\s(?:apples|cats|baseballs)\.',stories,re.I)
print(res)
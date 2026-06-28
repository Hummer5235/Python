import pyperclip

strings = pyperclip.paste()

listOfStrings = strings.split('\n')
for i in range(len(listOfStrings)):
	listOfStrings[i] = '*'+listOfStrings[i]#.replace('\r','')


print(listOfStrings)
text = '\n'.join(listOfStrings)
print(text)




# listOfStrings = ['Сегодня в гости я приехал к бабушке',
# 'В деревне пахнет летом',
# 'Много чего интересного я здесь увидел']
"""Сегодня в гости я приехал к бабушке
В деревне пахнет летом
Много чего интересного я здесь увидел"""



pyperclip.copy(text)




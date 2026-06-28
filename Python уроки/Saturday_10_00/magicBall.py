# Магический шар
import random
import time

print()
answer = input('Введите свой вопрос: ')
print('Готовлю ответ')
for i in range(3):
	time.sleep(random.randint(0,10)/10)
	print('...')
	time.sleep(random.randint(0,10)/10)
	print('.....')


messages = ['Это точно',
'Это определенно так',
'Мой ответ - да',
'Ответ туманный , попробуйте еще раз',
'Спросите позже',
'Сконцентрируйтесь и спросите еще раз',
'Мой ответ - нет',
'Перспективы не очень хорошие',
'Очень сомнительно']

answer = messages[random.randint(0,len(messages)-1)]
print(answer)

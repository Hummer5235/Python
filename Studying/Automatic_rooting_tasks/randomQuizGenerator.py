# Создает экзаменационные билеты с вопросами и ответами, расположенными в случайном порядке, вместе с ключами ответов

import random
# Данные билета. Ключи - названия штатов, а значения - столицы.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California':
'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota':
'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}


#Генерация 35 файлов билетов.

for quizNum in range(1,36):
	#Создать файлы билетов и ключей ответов.
	#Записать заголовок билета.
	#Перемешать порядок следования штатов
	#Организовать цикл по всем 50 штатам,
	#создавая вопрос для каждого из них

	file = open(rf'quizQuestions\{str(quizNum)}.txt','w')
	# file = open(r'quizQuestions\'+str(quizNum)+'.txt','w')
	keys = list(capitals.keys())
	values = list(capitals.values())
	for i in range(50):
		random_capital = keys[random.randint(0,49)]
		random_city = values[random.randint(0,49)]
		file.write(f'{i+1}. Является ли {random_city} столицей {random_capital}? Да[] \\ Нет[] \n')

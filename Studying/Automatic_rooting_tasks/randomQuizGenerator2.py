# Создает экзаменационные билеты с вопросами и ответами, расположенными в случайном порядке, вместе с ключами ответов

import random
import os
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
for quizNum in range(35):
	#Создать файлы билетов и ключей ответов.
	src1 = os.path.join('quizQuestions','V2','capitalsquiz')
	src2 = os.path.join('quizQuestions','V2','Answers','capitalsquiz_answers')
	quizFile = open(f'{src1}{quizNum+1}.txt','w')

	answerKeyFile = open(f'{src2}{quizNum+1}.txt','w')

	#Записать заголовок билета.
	quizFile.write('Имя:\n\nДата:\n\nКурс\n\n')
	quizFile.write(' '*15+f'Проверка знания столиц штатов (Билет {quizNum+1})')
	quizFile.write('\n\n')

	#Перемешать порядок следования штатов
	states = list(capitals.keys())
	random.shuffle(states)

	#Организовать цикл по всем 50 штатам,
	#создавая вопрос для каждого из них
	for questionNum in range(50):
		#Получение правильных и неправильных ответов.
		#Сохраняем правильный ответ
		correctAnswer = capitals[states[questionNum]] 
		wrongAnswers = list(capitals.values())

		#Удаляем правильный ответ из списка ложных
		del wrongAnswers[wrongAnswers.index(correctAnswer)]

		#Берем 3 случайных ложных ответа
		wrongAnswers = random.sample(wrongAnswers,3)

		#Добавляем в список правильный ответ
		answerOptions = wrongAnswers + [correctAnswer]

		#Перемешиваем список
		random.shuffle(answerOptions)
		



		#Запись вариантов вопросов и ответов в файл билета.
		quizFile.write(f'{questionNum+1}.Выберите столицу штата {states[questionNum]}:\n')
		for i in range(4):
			quizFile.write(f'{"ABCD"[i]}, {answerOptions[i]}')
			quizFile.write('\n')
		quizFile.write('\n')

		#Запись ключа ответа в файл.
		answerKeyFile.write(f'{questionNum+1}.{"ABCD"[answerOptions.index(correctAnswer)]}\n')
quizFile.close()
answerKeyFile.close()
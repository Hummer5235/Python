#Игра  виселица
import random,time

words = ['человек','клавиатура','букварь','время','океан','досуг','дерево','белуга','память','представление','страсть']


def get_word():
	return random.choice(words).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
	new_word = ''
	for i in word:
		new_word += i+'.'
	word = new_word
	word_completion = ''
	for i in word:
		if i != '.':
			word_completion += '_'
		else:
			word_completion += '.'
	right_letters = 0 # количество правильных названных букв
	guessed = False # сигнальная метка
	guessed_letters = [] # список уже названных букв
	guessed_words = [] # список уже названных букв
	tries = 6 # количество попыток

	print('Давай сыграем в одну игру!')
	time.sleep(2)
	print('Это угадайка слов!')
	time.sleep(2)
	while tries != 0:
		print(f'Количество попыток: {tries}')
		print(f'Слово: {word_completion}')
		letter = input('\nВведите букву: ').upper()

		if letter not in guessed_letters:
			guessed_letters.append(letter)
			if letter not in word:
				tries -= 1
				print('Это неверная буква')
			else:
				print('Это правильная буква, молодец!')
				right_letters += word.count(letter)
		else:
			print('Такая буква уже была введена - попытка не засчитана')


		for i in range(len(word)):
			if letter == word[i]:
				word_completion = word_completion[:i]+letter+word_completion[i+1:]
		
		#Проверка количества угаданных букв
		if right_letters == len(word)//2: 
			print('\nПоздравляем, вы отгадали слово!')
			print(f'Это было слово {word}')
			break
		
		print(display_hangman(tries))

		

	else:
		print('К сожалению вы проиграли')




answer = 'д'
while answer == 'д':
	word = get_word()
	play(word)
	answer = input('Сыграем еще раз? (д = да, н = нет): ')
	print()

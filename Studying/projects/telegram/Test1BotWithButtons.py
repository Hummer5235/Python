import telebot
from telebot import types # Для создания кнопок


bot = telebot.TeleBot('')

name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = types.InlineKeyboardMarkup() #клавиатура
    key_reg = types.InlineKeyboardButton(text='Регистрация',callback_data='yes registraion')
    key_help = types.InlineKeyboardButton(text='Помощь',callback_data='help')
    keyboard.add(key_reg)
    keyboard.add(key_help)
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Чем могу помочь?')
    else:
        bot.send_message(message.from_user.id, 'Нажмите "Регистрация"',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == 'yes registraion':
        bot.send_message(call.message.chat.id, 'Как тебя зовут?')
        bot.register_next_step_handler(call.message, get_name)
    elif call.data == 'help':
        bot.send_message(call.message.chat.id, 'Наши сотрудники:\n'
                                               '1. Создатель: Захар Шлыков https://vk.com/wase33\n'
                                               '2. Редактор: Ульяна Румянцева https://vk.com/uliana_r')
    elif call.data == 'correctly':
        bot.send_message(call.message.chat.id, f'{name} {surname}, Вы успешно зарегистрированы!')
    elif call.data == 'incorrectly':
        correction_of_data(call)
    elif call.data == 'name incorrect':
        bot.send_message(call.message.chat.id, 'Как тебя зовут?')
        bot.register_next_step_handler(call.message, get_name, 'yes')
    elif call.data == 'surname incorrect':
        bot.send_message(call.message.chat.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(call.message, get_surname, 'yes')
    elif call.data == 'age incorrect':
        bot.send_message(call.message.chat.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(call.message, get_age, 'yes')

def correction_of_data(call):
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_name = types.InlineKeyboardButton(text='Имя', callback_data='name incorrect')
    key_surname = types.InlineKeyboardButton(text='Фамилия', callback_data='surname incorrect')
    key_age = types.InlineKeyboardButton(text='Возраст', callback_data='age incorrect')
    keyboard.add(key_name)
    keyboard.add(key_surname)
    keyboard.add(key_age)
    bot.send_message(call.message.chat.id, 'Давайте попробуем еще раз')
    bot.send_message(call.message.chat.id, 'Что нужно исправить: Имя? Фамилия? Возраст?',reply_markup=keyboard)



def get_name(message,correction=None):
    global name
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='correctly')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='incorrectly')
    keyboard.add(key_yes)
    keyboard.add(key_no)
    name = message.text
    if correction == None:
        bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(message, get_surname)
    else:
        bot.send_message(message.from_user.id, 'Имя успешно изменено')
        bot.send_message(message.from_user.id, f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                               f': {surname}\nage: {age}',reply_markup=keyboard)
        # bot.register_next_step_handler(message,check_data)



def get_surname(message,correction=None):
    global surname
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='correctly')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='incorrectly')
    keyboard.add(key_yes)
    keyboard.add(key_no)
    surname = message.text
    if correction == None:
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Фамилия успешно изменена')
        bot.send_message(message.from_user.id, f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                               f': {surname}\nage: {age}',reply_markup=keyboard)
        # bot.register_next_step_handler(message,check_data)

def get_age(message,correction = None):
    global age
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='correctly')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='incorrectly')
    keyboard.add(key_yes)
    keyboard.add(key_no)
    try:
        age = int(message.text)
    except:
        bot.send_message(message.from_user.id, 'Цифрами пожалуйста :)')
        bot.register_next_step_handler(message, get_age)
    else:
        if correction != None:
            bot.send_message(message.from_user.id,'Возраст успешно изменен')
        bot.send_message(message.from_user.id,f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                              f': {surname}\nage: {age}',reply_markup=keyboard)
        # check_data()
        # bot.register_next_step_handler(message, check_data)

def check_data(message,answer):
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_name = types.InlineKeyboardButton(text='Имя', callback_data='name incorrect')
    key_surname = types.InlineKeyboardButton(text='Фамилия', callback_data='surname incorrect')
    key_age = types.InlineKeyboardButton(text='Возраст', callback_data='age incorrect')
    keyboard.add(key_name)
    keyboard.add(key_surname)
    keyboard.add(key_age)
    # answer = message.text.lower()
    # if answer == 'да' or answer == 'yes':
    #     bot.send_message(message.from_user.id, f'{name} {surname}, Вы успешно зарегистрированы!')
    # else:
    # bot.send_message(message.from_user.id, 'Давайте попробуем еще раз')
    # bot.send_message(message.from_user.id, 'Что нужно исправить: Имя? Фамилия? Возраст?',reply_markup=keyboard)
        # bot.register_next_step_handler(message, correction_of_data)

# def correction_of_data(message):
#     answer = message.text.lower()
#     if answer == 'имя':
#         bot.send_message(message.from_user.id, 'Как тебя зовут?')
#         bot.register_next_step_handler(message, get_name,'yes')
#     elif answer == 'фамилия':
#         bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#         bot.register_next_step_handler(message, get_surname,'yes')
#     elif answer == 'возраст':
#         bot.send_message(message.from_user.id, 'Сколько тебе лет?')
#         bot.register_next_step_handler(message, get_age,'yes')
#     else:
#         bot.send_message(message.from_user.id, 'Попробуйте зарегистрироваться заново')
#         # bot.register_next_step_handler(message, start)

# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#     if message.text == '/start':
#         print('Старт')
#     elif message.text.lower() == 'привет':
#         bot.send_message(message.from_user.id,f'Привет {message.from_user.username}! Чем могу помочь? ')
#         print(f'Привет! Чем могу помочь? ')


bot.polling(none_stop=True,interval=0)
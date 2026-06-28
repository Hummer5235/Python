import telebot
from telebot import types # Для создания кнопок


bot = telebot.TeleBot('')

name = ''
surname = ''
age = 0

# data = ['','','']

#Отлавливаем команды
# @bot.message_handler(commands=['start'])
# def url(message):
#     markup  =   types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Наш сайт',url='https://github.com')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id,'По кнопке ниже можно перейти на наш сайт',reply_markup=markup)


# @bot.message_handler(commands=['vk'])
# def url(message):
#     markup  =   types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Наш сайт',url='https://vk.com')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id,'По кнопке ниже можно перейти на наш сайт',reply_markup=markup)



@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = types.InlineKeyboardMarkup() #клавиатура
    key_reg = types.InlineKeyboardButton(text='Регистрация')
    keyboard.add()
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напишите /reg')



def get_name(message,correction=None):
    global name
    name = message.text
    if correction == None:
        bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(message, get_surname)
    else:
        bot.send_message(message.from_user.id, 'Имя успешно изменено')
        bot.send_message(message.from_user.id, f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                               f': {surname}\nage: {age}')
        bot.register_next_step_handler(message,check_data)


def get_surname(message,correction=None):
    global surname
    surname = message.text
    if correction == None:
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Фамилия успешно изменена')
        bot.send_message(message.from_user.id, f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                               f': {surname}\nage: {age}')
        bot.register_next_step_handler(message,check_data)

def get_age(message,correction = None):
    global age
    try:
        age = int(message.text)
    except:
        bot.send_message(message.from_user.id, 'Цифрами пожалуйста :)')
        bot.register_next_step_handler(message, get_age)
    else:
        if correction != None:
            bot.send_message(message.from_user.id,'Возраст успешно изменен')
        bot.send_message(message.from_user.id,f'Давайте проверим введенные данные. Все верно?\nname: {name}\nsurname'
                                              f': {surname}\nage: {age}')
        bot.register_next_step_handler(message, check_data)

def check_data(message):
    answer = message.text.lower()
    if answer == 'да' or answer == 'yes':
        bot.send_message(message.from_user.id, f'{name} {surname}, Вы успешно зарегистрированы!')
    else:
        bot.send_message(message.from_user.id, 'Давайте попробуем еще раз')
        bot.send_message(message.from_user.id, 'Что нужно исправить: Имя? Фамилия? Возраст?')
        bot.register_next_step_handler(message, correction_of_data)

def correction_of_data(message):
    answer = message.text.lower()
    if answer == 'имя':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name,'yes')
    elif answer == 'фамилия':
        bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
        bot.register_next_step_handler(message, get_surname,'yes')
    elif answer == 'возраст':
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age,'yes')
    else:
        bot.send_message(message.from_user.id, 'Попробуйте зарегистрироваться заново')
        # bot.register_next_step_handler(message, start)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        print('Старт')
    elif message.text.lower() == 'привет':
        bot.send_message(message.from_user.id,f'Привет {message.from_user.username}! Чем могу помочь? ')
        print(f'Привет! Чем могу помочь? ')


bot.polling(none_stop=True,interval=0)
import os, time
from telegram_api import send_message

def output(result,timelength):
    if result:
        # print(*result.items(), sep='\n')
        dict_formatter(result,timelength)
    else:
        t = time.strftime('%H:%M:%S', time.localtime())
        print(result,t)


def dict_formatter(dictionary:dict,time_length):
    string = ''
    for carriage_number in dictionary:
        string += 'Вагон '+carriage_number+':\n'
        for place,placeType in dictionary[carriage_number].items():
            string+=place+' '+placeType+'\n'
        string += '\n'
    string = f'Время с последнего изменения: {time_length}\nЕсть результат:\n\n{string}'
    print(string)
    send_message(string)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
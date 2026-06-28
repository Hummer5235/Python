from Telegram_Api import send_start_message, send_messages, error_notification, get_updates
from Date import get_date,get_time, get_datetime, is_time_to_start, read_date, write_date
from Numbers_Api import get_fact
from Googletrans_Api import get_translate
from Logger import *

MINUTES_TIMEOUT = 15
START_TIME = 0
RESTART_COUNTER = 0
day, month = read_date()




def main():
    global day,month
    while True:
        get_updates()
        if is_time_to_start(day):
            day, month = get_date()
            write_date(day,month)
            fact = get_fact(month, day)
            text = get_translate(fact)
            send_messages(text)
        print('Текущая дата:',day+'-'+month,'Время:',get_time())
        print('Время работы программы:',(get_datetime()-START_TIME), 'Количество перезапусков программы:',RESTART_COUNTER)
        print('-------------------------')
        logging.info(f"successful result")


if __name__ == '__main__':
    send_start_message() #Сообщение в тг о запуске
    while True:
        try:
            START_TIME = get_datetime()
            while True:
                main()
                RESTART_COUNTER += 1
        except:
            logging.exception("Error")





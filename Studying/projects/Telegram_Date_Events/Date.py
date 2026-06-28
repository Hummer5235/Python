import datetime
from time import sleep

date = None

def read_date():
    with open('date.txt') as file:
        date = file.readline()
        day, month = date.split('-')
        return day,month

def write_date(day,month):
    with open('date.txt','w') as file:
        file.write(f'{day}-{month}')

def get_date()-> (str,str):
    global date
    date = datetime.datetime.now()
    day,month =  str(date.date()).split('-')[:0:-1]
    return day,month

def get_time()->datetime:
    time = datetime.datetime.now().time()
    return time

def get_datetime()->datetime:
    d_time = datetime.datetime.now()
    return d_time

def time_formatter(time: datetime) -> int :
    time = str(time).split(':')
    hour = int(time[0])
    return hour


def is_time_to_start(day:str):
    current_day, month = get_date()
    if current_day != day:
        time = get_time()
        time = time_formatter(time)
        if 12 > time >= 10:
            return True



# print(str(is_time_to_start()))


from  time import  sleep
from datetime import datetime
# date — хранит дату
# time — хранит время
# datetime — хранит дату и время


#
# for i in range(51):
#     time_obj = time(10, 0, i)
#     sleep(1)
#     print(time_obj)


second_date = datetime.now()
first_date = datetime.strptime(input('Введите дату: '),"%d %b %Y %H:%M")
# first_date = datetime.strptime(input('Введите дату: '),"%d %b %Y %H:%M")
print(second_date-first_date)



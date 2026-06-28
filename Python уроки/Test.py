def find_student_data(string):
    index_price = string.index(')') + 1
    student_string = string[index_price:]
    student_data = student_string.replace(' ', '').replace('\n', '').split(',')
    return student_data

message = '''Ваня(1200)7
Тимур(1500) 5
Ярослав (1500)6
Коля(1300) 6,7
Саша Третьяков (1500)
Марк(1500) 5
Итан(2000) _
Даня Ольга(2000) 
Денис Оксана(1500) 5
Артем Захарченко(1500) 7, 5
Леша(1500) -6 
Георгий(1500) 5
Кирилл(1500)
Тимофей(1700)7
Платон (2500)-6,-7
Даня Продвинутый(1800)6
Артем Оксана (1500) 6
Степан(1800)6'''

for string in message.split('\n'):
    answer = find_student_data(string)
    print(answer)
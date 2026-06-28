


def find_price(string):
    if '(' in string and ')' in string:
        return int(string[string.index('(') + 1:string.index(')')])
    else:
        return 0

def find_student_data(string):
    index_price = string.index(')') + 1
    student_string = string[index_price:]
    student_data = student_string.replace(' ', '').replace('\n', '').split(',')
    return student_data

def count_dates(student_data):
    lessons = 0
    for date in student_data:
        # Не считать урок за этот месяц, если оплата на следующий месяц
        if '+' not in date:
            lessons += 1
    return lessons


def count_payments(message:str):
    summa = 0
    lessons = 0
    message = message.split('\n')
    for string in message:
        price = find_price(string)
        if price != 0:
            student_data = find_student_data(string)
            lessons = count_dates(student_data)
        summa += price * lessons
    return summa




if __name__ == '__main__':
    count_payments()




def find_price(string):
    if '(' in string and ')' in string:
        return int(string[string.index('(') + 1:string.index(')')])
    else:
        return None

def find_student_data(string):
    index_price = string.index(')') + 1
    student_string = string[index_price:]
    dates = student_string.replace(' ', '').replace('\n', '').split(',')
    student_data = []
    for element in dates:
        if element.isdigit():
            student_data.append(element)
    return student_data

def count_dates(student_data):
    lessons = 0
    for date in student_data:
        # Не считать урок за этот месяц, если оплата на следующий месяц, неоплачено или не цифра
        if date.isdigit():
            lessons += 1
    return lessons


def count_payments(message:str):
    summa = 0
    lessons = 0
    message = message.split('\n')

    for string in message:
        price = find_price(string)
        if price != None:
            student_data = find_student_data(string)
            lessons = count_dates(student_data)
            summa += price * lessons
    return summa




if __name__ == '__main__':
    count_payments()

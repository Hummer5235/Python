def find_price(string):
    return int(string[string.index('(') + 1:string.index(')')])

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


def main():
    with open('payments.txt',encoding='utf-8') as file:
        summa = 0
        for string in file:
            price = find_price(string)
            student_data = find_student_data(string)
            lessons = count_dates(student_data)
            summa += price*lessons
        print(f'Сумма за месяц: {summa} Руб.')



if __name__ == '__main__':
    main()

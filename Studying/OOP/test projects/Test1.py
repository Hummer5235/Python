def create_new_student():
    name = input('Введите полное имя: ')
    old = int(input('Введите ваш возраст: '))
    course_name = input('Введите направление курса: ')
    course_number = int(input('Введите номер курса: '))

    return name, old, course_name, course_number


class Student:

    def __init__(self, full_name, old, course_name, course_number ):

        self.__full_name = full_name
        self.__old = old
        self.__course_name = course_name
        self.__course_number = course_number

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value




# st1 = Student(*create_new_student())



st1 = Student('Жужаков Григорий Александрович', 23, 'Горная специальность', 5)

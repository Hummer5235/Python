

class Check:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):

        print(f'__set__: {self.name} = {value}')
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Student:
    full_name = Check()
    # old = Check()
    course_name = Check()
    course_number = Check()

    def __init__(self, full_name, old, course_name, course_number):
        self.full_name = full_name
        self.old = old
        self.course_name = course_name
        self.course_number = course_number

    # def create_new_student(self):
    #     self.__full_name = input('Введите полное имя: ')
    #     self.__old = int(input('Введите ваш возраст: '))
    #     self.__course_name = input('Введите направление курса: ')
    #     self.__course_number = int(input('Введите номер курса: '))

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value




# st1 = Student(*create_new_student())
st1 = Student('Жужаков Григорий Александрович', 23, 'Горная специальность', 5)
# st1 = Student()
# print(st1.__x)
print(st1.__dict__)



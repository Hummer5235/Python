class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 120 and age >= 0:
            self.__age = age
        else:
            self.__age = 0

    age = property(get_age, set_age)
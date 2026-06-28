class Player:

    def __new__(cls, *args, **kwargs):
        print(f'Вызов метода __new__')
        return object.__new__(cls)

    def __init__(self,name, health, lvl):
        self.verify_health(health)
        self.__name = name
        self.__health = health
        self.__lvl = lvl

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if self.verify_health(value):
            self.__health = value
    @classmethod
    def verify_health(self, value):
        if type(value) in (int,float):
            return True
        else:
            raise TypeError('Здоровье должно быть написано цифрами')



p1= Player('Henry', 100, 5)
print(p1.__dict__)
print(p1.health)
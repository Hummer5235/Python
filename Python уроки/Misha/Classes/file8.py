#__str__ - магический метод для отображения информации об объекте класса для пользователей
#__repr__ - магический метод для отображения информации об объекте класса в режиме отладки

class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'{self.__class__}:{self.name}'

    def __str__(self):
        return f'{self.name}'


cat1 = Cat('Алиса','египетская')
cat2 = Cat('Барсик','обычный')


print(cat1)
print(cat2)

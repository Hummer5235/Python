class Cat:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f'{self.name}'

    def say(self):
        print(f'Меня зовут {self.name}')



cat1 = Cat('Барсик','Мейн-Кун')
cat2 = Cat('Смоки','Британский серый')

cat1.say()
cat2.say()
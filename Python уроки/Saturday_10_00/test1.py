# import random
from random import randint, randrange
# from random import *
words = ['Стол','Стул','Экран','Колонки','Окно','Дверь',
         'Ложка','Вилка','Нож','Батарея','Дерево','Зелень','Колесо','Диск','Качели']


# for i in range(10):
#     r = random.randint(0,14)
#     print(words[r])


for i in range(10):
    r = randint(0,14)
    print(words[r])

# print(*[words[randint(0,14)] for i in range(10)],sep='\n')
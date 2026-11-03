
'''
    class Имя_Класса:
        Атрибуты (Переменные)

        Методы (Самостоятельные функции)

'''

class Monster:

    def __init__(self,name,character):#Конструктов. Вызывается автоматически при создании объекта
        #Атрибуты (Свойства)
        self.Name = name
        self.Character = character

    #Метод (функция, действие)
    def show(self):
        print('Имя:',self.Name)
        print('Особенность:',self.Character)


Alex = Monster('Алекс','Странный')#Создание объекта
# Alex.show()

Bob = Monster('Боб','Скверный')

Alex.show()
Bob.show()



#НАСЛЕДОВАНИЕ - создание нового класса (подкласс или дочерний класс) на основе уже существующего

'''
    class дочерний(родительский):
        Атрибуты + наследуемые атрибуты
        
        Методы + наследуемые методы
'''



class SMonster(Monster): #Наследовали от Класса Monster
    pass


class GMonster(Monster): #Наследовали от Класса Monster
    pass

Victor = SMonster('Виктор','Милый')

Mark - GMonster



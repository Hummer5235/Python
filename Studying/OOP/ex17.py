#17. Магический метод __bool__ определения правдивости объектов
#Правдивость - когда к экз класса явно или неявно применяется функция bool
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __len__(self):
        print('вызов __len__')
        return self.x * self.x +self.y * self.y
    

    def __bool__(self):
        print('вызов __bool__')
        #Обязательно возвращает логическое значение
        
        return self.x == self.y


#Изначально функция bool 

p = Point(3,4)
print(bool(p))
# print(len(p))

#__bool__ неявно используется в условных операторах
if p:
    print('Объект p дает True')
else:
    print('Объект p дает False')
    
    
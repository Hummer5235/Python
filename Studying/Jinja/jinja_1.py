from jinja2 import Template

name = "Федор"
age = 25

tm = Template("Мне {{a}} лет и зовут {{n.upper()}}.") # Создаем экземпляр класса Template на основе шаблона
msg = tm.render(n = name, a = age) # Происходит рендер, и возвращает готовый обработанный шаблон
# Метод render - формируем словарь значений где n и a - ключи
# n,a - именованные параметры
# С помощью класса Template мы можем передавать конструкции Python , а не просто переменные



print(msg)

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age

per = Person("Федор",33)

tm = Template("Мне {{p.age}} лет и зовут {{p.name}}.") # Создаем экземпляр класса Template на основе шаблона
msg = tm.render(p = per)
# Внутри шаблона нам  доступны ссылки переданные в методе render
print(msg)

# С помощью геттеров
tm = Template("Мне {{p.getAge()}} лет и зовут {{p.getName()}}.") # Создаем экземпляр класса Template на основе шаблона
msg = tm.render(p = per)

print(msg)

#С помощью словаря
per = {"name":"Федор","age":"34"}
tm = Template("Мне {{p['age']}} лет и зовут {{p['name']}}.")
msg = tm.render(p = per)
print(msg)
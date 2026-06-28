#4: Загрузчики шаблонов - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader

from jinja2 import Template,FileSystemLoader,Environment,FunctionLoader

users = [{"name":"Андрей","old":25,"weight":85},
        {"name":"Иван","old":29,"weight":82},
        {"name":"Алексей","old":23,"weight":76},
        {"name":"Николай","old":13,"weight": 58},
        {"name":"Женя","old":32,"weight":94}]

def loadTpl(path):
        if path == "index":
                return '''Имя {{u.name}}, возраст {{u.old}}'''
        else:
                return '''Данные: {{u}}'''

# file_loader = FileSystemLoader("templates") # Файловый загрузчик. Папка с шаблонами
file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader) # Окружение

tm = env.get_template("index2") # Формирует экз класса Template на основе содержимого файла main.htm
msg = tm.render(u = users[0])
print(msg)



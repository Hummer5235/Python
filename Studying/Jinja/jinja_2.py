#2: Экранирование и блоки raw, for, if
# Экранирование данных в строках
from jinja2 import Template

data = """Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение"""

tm = Template(data)
msg = tm.render(name = "Федор")
print(msg,end="\n\n")

# Если необходимо никак не изменять значение data используем блок raw
data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render()
print(msg,end="\n\n")

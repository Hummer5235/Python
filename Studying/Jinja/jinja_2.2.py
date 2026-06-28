#2: Экранирование и блоки raw, for, if
from jinja2 import Template
from markupsafe import escape
'''Формируем из имеющегося списка список для нашего HTML документа.
Внутри тега select будут прописаны соответствующие строки на основе списка cities'''


cities = [{"id":1,"city":"Москва"},
          {"id":5,"city":"Тверь"},
          {"id":7,"city":"Минск"},
          {"id":8,"city":"Смоленск"},
          {"id":11,"city":"Калуга"}]

"""Будем перебирать коллекцию cities """
# -% Используем для удаления пробела между строками

link =''' <select name = 'cities'>
{% for c in cities -%}
    <option value = "{{c.id}}" >{{c.city}}</option>
{% endfor -%}
</select>'''
tm = Template(link)
msg = tm.render(cities = cities)

print(msg)

#
# link= '''<select name = 'cities'>
# {% for c in cities -%}
# {% if c.id > 6 -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% elif c.city=="Москва" -%}
#     <option>{{c['city']}}</option>
# {% else -%}
#     {{c['city']}}
# {% endif -%}
# {% endfor -%}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities = cities)
#
# print(msg)
#

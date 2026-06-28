#3: Фильтры и макросы macro, call

from jinja2 import Template

users = [{"name":"Андрей","old":25,"weight":85},
        {"name":"Иван","old":29,"weight":82},
        {"name":"Алексей","old":23,"weight":76},
        {"name":"Николай","old":13,"weight": 58},
        {"name":"Женя","old":32,"weight":94}]
tpl = """
{%for u in users-%}
{%filter upper%}{{u.name}}{%endfilter%}
{%endfor-%}
"""
tm = Template(tpl)
msg = tm.render(users = users)
print(msg)


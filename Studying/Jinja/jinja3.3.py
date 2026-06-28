#3: Макрос macro

from jinja2 import Template

users = [{"name":"Андрей","old":25,"weight":85},
        {"name":"Иван","old":29,"weight":82},
        {"name":"Алексей","old":23,"weight":76},
        {"name":"Николай","old":13,"weight": 58},
        {"name":"Женя","old":32,"weight":94}]
html = """
{%macro list_users(list_of_users)-%}
<ul>
{%for u in list_of_users-%}
        <li>{{u.name}}
{%endfor%}
</ul>
{%endmacro-%}
{{list_users(users)}}
"""

tm = Template(html)
msg = tm.render(users = users)
print(msg)

# Макрос call
# Добавляется вложеный список при вызове caller
# При вызове caller в него подставляется то, что написано внутри блока call
html = """
{%macro list_users(list_of_users)-%}
<ul>
{%for u in list_of_users-%}
        <li>{{u.name}}{{caller(u)}} 
{%endfor%}
</ul>
{%endmacro-%}

{% call(user) list_users(users)%}
<ul>
<li>age: {{user.old}}
<li>weight: {{user.weight}}
</ul>
{%endcall-%}
"""


tm = Template(html)
msg = tm.render(users = users)
print(msg)
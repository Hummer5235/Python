from jinja2 import Template


data = """{%raw%}Все что будет 
передано с помощью {{data}}
не будет изменено""{%endraw%}"""

tm = Template(data)
msg = tm.render(data = data)
print(msg)
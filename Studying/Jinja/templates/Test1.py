from jinja2 import Template
"""
# name = "Алексей"
# city = "Суздаль"
# 
# tm = Template("Меня зовут {{name}} , я из города {{city}}")
# message = tm.render(name = name,city = city)
# print(message)"""
#
#
# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template("{{link|e}}")
# message = tm.render(link = link)
# print(message)

#-------------------------------------------------------------------------

cities = [{"id":1,"city":"Москва"},
          {"id":5,"city":"Тверь"},
          {"id":7,"city":"Минск"},
          {"id":8,"city":"Смоленск"},
          {"id":11,"city":"Калуга"}]

# link ="""<names of cities >
# {%for i in cities-%}
#     <value = {{i.id}}><name = {{i.city}}>
# {%endfor-%}
# <end names>
# """
#
# tm = Template(link)
# message = tm.render(cities = cities)
# print(message)



link ="""<names of cities >
{%for i in cities-%}
{%if i.id  > 5 -%}
    <Город поменьше>
{%else-%}    
    <value = {{i.id}}><name = {{i.city}}>
{%endif-%}
{%endfor-%}
<end names>
"""
tm = Template(link)
message = tm.render(cities = cities)
print(message)

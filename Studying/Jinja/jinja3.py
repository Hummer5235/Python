#3: Фильтры и макросы macro, call

from jinja2 import Template

cars = [{"model":"Ауди","price":3500},
        {"model":"Шкода","price":2010},
        {"model":"Вольво","price":5000},
        {"model":"Лада","price":1500},
        {"model":"Фольксваген","price":4500}]

#sum - Фильтр для вычисления суммы определенной коллекции
tpl = "Суммарная стоимость автомобилей {{cs | sum(attribute = 'price')}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

digs = [1,2,3,4,5]

tpl = "Суммарная стоимость автомобилей {{cs | sum}}"


tm = Template(tpl)
msg = tm.render(cs = digs)
print(msg)

#sum - Фильтр для вычисления суммы определенной коллекции
tpl = "Суммарная стоимость автомобилей {{(cs | max(attribute = 'price')).model}}"

# Фильтр random
tpl2 = " Автомобиль {{cs | random }}"
# Фильтр replace
tpl3 = " Автомобиль {{cs | replace('о','О') }}"

tm = Template(tpl)
msg = tm.render(cs = digs)
print(msg)
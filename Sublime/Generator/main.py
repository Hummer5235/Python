#list comprehension

# Генераторы списков

some_list = [1,2]

things = [x for x in some_list ]

#(values) = [(expression) for (value) in (collection)]
"""expression - то, что будет добавляться в список
далее традиц объявление списка  цикла for"""
""" expression называется также как и value """



jack = {
    "name":"Jack",
    "car":"bmw"
}

john = {
    "name":"John",
    "car":"audi"
}

users = [jack,john] # Список словарей


# cars = []
#
# for person in users:
#     cars.append(person["car"])
# print(cars)


cars = [person.get("car","") for person in users]
print(cars)


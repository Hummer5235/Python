name = "Семен"
middle_name = "Семенович"
balance = "3700.00"

text = """\nДорогой {0} {1}, баланс вашего 
лицевого счета равен {2} рублей""".format(name,middle_name,balance)

print(text)

name2 = "Александр"
middle_name2 = "Петрович"
balance2 = "250.00"

text = """\nДорогой {name} {middle_name}, баланс вашего 
лицевого счета равен {balance} рублей""".format(name = name2,middle_name = middle_name2,balance=balance2)

print(text)


name3 = "Анатолий"
middle_name3 = "Анатольевич"
balance3 = "100.00"

text = f"""\nДорогой {name3} {middle_name3}, баланс вашего 
лицевого счета равен {balance3} рублей"""

print(text)

people = []

def about_human():
    human = []
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    address = input('Введите адрес: ')
    wish = True
    wishes = []
    print('Для завершения ввода желаний напишите "выход"')
    while wish :
        wish = input('Введите свое желание: ')
        if wish.lower() =='выход':
            break
        wishes.append(wish)
    human.append(name)
    human.append(age)
    human.append(address)
    human.append(wishes)
    people.append(human)
    print(people)
about_human()
about_human()

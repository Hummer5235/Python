# Метод get(key,default) - возвращает значение ключа, но если его нет , не выдает ошибку
# а возвращает default

persons = {"Misha":"+791522385","Seva":"+79602454415"}
answer = persons.get("Zahar","No key")
answer2 = persons.get("Misha","No key")
print(answer)
print(answer2)

# Метод setdefault() - возвращает значение ключа или добавляет ключ-значение в словарь
answer = persons.setdefault("Zahar","+79220740000")
answer2 = persons.setdefault("Misha","+79220740000")
print(answer)
print(answer2)
print(persons)


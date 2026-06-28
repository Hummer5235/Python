# SELECT ROWID, * FROM users WHERE ROWID>=2
# DROP TABLE users
# INSERT INTO users (name,old) VALUES ('Alice',12)
# SELECT * FROM users WHERE old >=12 AND old <25 AND score < 1000
# SELECT * FROM users WHERE old IN (10,12,16,25) AND score < 1000


#Составные условия
# AND – условное И: exp1 AND exp2. Истинно, если одновременно истинны exp1 и exp2.
# OR – условное ИЛИ: exp1 OR exp2. Истинно, если истинно exp1 или exp2 или оба выражения.
# NOT – условное НЕ: NOT exp. Преобразует ложное условие в истинное и, наоборот, истинное – в ложное.
# IN – вхождение во множество значений: col IN (val1, val2, …)
# NOT IN – не вхождение во множество значений: col NOT IN (val1, val2, …)


# Создается выборка из игроков возрастом 19 или 32 года и числом очков менее 1000. Следующий запрос:
# SELECT * FROM users WHERE old IN(19, 32) AND score < 1000


# SELECT * FROM users WHERE old IN(19, 32) AND score > 300 OR sex = 1
# Выберет все записи из таблицы users. Здесь фильтр будет работать так: выбираются
# игроки возрастом 19 или 32 года и числом очков более 300 или те, у которых мужской пол (sex = 1).
# И, так как у нас все игроки имеют мужской пол, то все они и будут отображены в результатах
# отбора. Этот пример показывает важность приоритетов: приоритет у операции AND выше, чем у OR,
# поэтому AND выполняется раньше OR.


# Сортировка ORDER BY
# После условия в команде SELECT можно дополнительно указывать сортировку записей по определенному
# столбцу. Предположим, что мы хотим выбрать всех игроков с числом очков менее 1000 и
# отсортировать их по возрастанию возраста. Это можно сделать так:
# SELECT * FROM users WHERE score < 1000 ORDER BY old

# Если нужно отсортировать данные по убыванию, то после имени поля следует указать флаг DESC:
# SELECT * FROM users WHERE score < 1000 ORDER BY old DESC

import sqlite3 as sq



# with sq.connect("chinook.db") as con:  # Менеджер контекста
#     cur = con.cursor()
#     cur.execute("""SELECT Title,ArtistId FROM albums WHERE ArtistId < 50 ORDER BY ArtistId""")
#     res = cur.fetchmany(10)
#     for i in res:
#        print(i)

with sq.connect("chinook.db") as con:  # Менеджер контекста
    cur = con.cursor()
    cur.execute("""SELECT CustomerId,FirstName,LastName FROM customers WHERE Country LIKE 'Brazil' ORDER BY CustomerId""")
    res = cur.fetchmany(10)
    for i in res:
       print(i)

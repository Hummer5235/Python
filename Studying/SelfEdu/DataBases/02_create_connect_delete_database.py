import sqlite3 as sq

# con = sq.connect("snake.db") #установить связь с определенной БД. Файл либо будет открыт, либо будет создан, если он не существует
# cur = con.cursor()
#
# cur.execute("""
# """)               # Запрос к базе данных
#
# con.close()



with sq.connect("users.db") as con:  # Менеджер контекста
    cur = con.cursor()
    cur.execute("""CREATE TABLE users (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        score INTEGER
    )""")


#Типы полей
# NULL – значение NULL;
# INTEGER – целочисленный тип (занимает от 1 до 8 байт);
# REAL – вещественный тип (8 байт в формате IEEE);
# TEXT – строковый тип (в кодировке данных базы, обычно UTF-8);
# BLOB (двоичные данные, хранятся «как есть», например, для небольших изображений).
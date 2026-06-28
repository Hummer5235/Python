import sqlite3 as sq

with sq.connect('weather.db') as con:
    cur = con.cursor() #Используем курсор для взаимодействия с БД
    # cur.execute('''DROP table cities''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cities (
    title TEXT

    )''')
    # cur.execute('''
    # INSERT INTO cities VALUES('Кострома')
    # ''')
    # for i in range(1000000):
    #     cur.execute(f'''INSERT INTO cities VALUES('{i}')''')
    #
    # cur.execute('''INSERT INTO cities VALUES('Москва')''')


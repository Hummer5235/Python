import sqlite3 as sq


book_data = [
('Мастер и Маргарита','Булгаков М.А.',670.99,3),
('Белая гвардия','Булгаков М.А.',540.50,5),
('Идиот','Достоевский Ф.М.',460,10),
('Братья Карамазовы','Достоевский Ф.М.',799.01,2)
]

with sq.connect("book.db") as con:  # Менеджер контекста
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS book(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        price INTEGER,
        amount INTEGER
    )""")
    cur.executemany("INSERT INTO book(title,author,price,amount) VALUES(?,?,?,?)",book_data)

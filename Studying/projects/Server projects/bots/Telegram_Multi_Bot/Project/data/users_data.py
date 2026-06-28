import os
import sqlite3 as sq


current_path = os.path.dirname(os.path.abspath(__file__))

# Начальный словарь - шаблон данны пользователя
user_dict = {'username': 0,
        'in_game': 0,
        'secret_day': 0,
        'secret_month': 0,
        'event': 0,
        'attempts': 0,
        'total_games': 0,
        'wins': 0,
        'day_event_mailing':0,
        'bot_messages_ids':[],
        'user_messages_ids':[]
             }

# Список, в котором хранятся id администраторов
ADMIN_IDS = [852757379]

# Хранилище ожидающих пользователей
waiting_users = {}

# Словарь, в котором будут храниться данные пользователей
users = {}


def read_users_data():
    try:
        with sq.connect(current_path+'/users.db') as con:
            con.row_factory = sq.Row
            cur = con.cursor()
            cur.execute("""SELECT * from users""")
            records = cur.fetchall()
            for row in records:
                row = dict(row)
                print(row)
                user = row['user_id']
                users[user] = user_dict.copy()
                users[user]['username']= row['username']
                users[user]['in_game']= row['in_game']
                users[user]['secret_day']= row['secret_day']
                users[user]['secret_month']= row['secret_month']
                users[user]['event']= row['event']
                users[user]['attempts']= row['attempts']
                users[user]['total_games']= row['total_games']
                users[user]['wins']= row['wins']
                users[user]['day_event_mailing'] = row['day_event_mailing']
            print('Чтение базы данных успешно завершено')
    except:
        print('Ошибка чтения базы данных')


    
def update_users_data(user):
    user_id = user.id
    username=user.username
    try:
        with sq.connect(current_path + '/users.db') as con:
            cur = con.cursor()

        # Обновить данные всех пользователей

            cur.execute("""
                        UPDATE users
                        SET username = ?, 
                        in_game = ?,
                        secret_day = ?,
                        secret_month = ?,
                        event = ?,
                        attempts = ?,
                        total_games = ?,
                        wins = ?,
                        day_event_mailing = ?
                        WHERE user_id IS ?
                    """,

                        [username,
                         users[user_id]['in_game'],
                         users[user_id]['secret_day'],
                         users[user_id]['secret_month'],
                         users[user_id]['event'],
                         users[user_id]['attempts'],
                         users[user_id]['total_games'],
                         users[user_id]['wins'],
                         users[user_id]['day_event_mailing'],
                         user_id]
                        )
        users[user_id]['username'] = username
        print('Обновление базы данных успешно завершено',user_id,username,users[user_id])
    except:
        print('Ошибка обновления базы данных', user_id,username,users[user_id])

def write_users_data(user):
    user_id = user.id
    username = user.username
    try:
        with sq.connect(current_path+'/users.db') as con:
            cur = con.cursor()

            #Создать таблицу в случае отсутствия
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                "user_id"	INTEGER,
                "username"	TEXT,
                "in_game"	INTEGER,
                "secret_day"	INTEGER,
                "secret_month"	TEXT,
                "event"	TEXT,
                "attempts"	INTEGER,
                "total_games"	INTEGER,
                "wins"	INTEGER,
                "day_event_mailing"	INTEGER
            )""")

            #Добавить пользователя в БД в случае отсутствия
            cur.execute("""INSERT INTO users(
                        user_id ,
                        username,
                        in_game ,
                        secret_day ,
                        secret_month ,
                        event ,
                        attempts ,
                        total_games ,
                        wins,
                        day_event_mailing
                    )
                    VALUES
                    (?,?,?,?,?,?,?,?,?,?)
                    """,
                        [user_id,
                         username,
                         user_dict['in_game'],
                         user_dict['secret_day'],
                         user_dict['secret_month'],
                         user_dict['event'],
                         user_dict['attempts'],
                         user_dict['total_games'],
                         user_dict['wins'],
                         user_dict['day_event_mailing']]
                        )
        print('Запись в базу данных успешно завершена')
        users[user_id] = user_dict.copy()
        users[user_id]['username'] = username
    except:
        print('Ошибка записи в базу данных')

import os
import pickle
import sqlite3 as sq

current_path = os.path.dirname(os.path.abspath(__file__))



# Начальный словарь - шаблон данны пользователя
user_dict = {'in_game': 0,
        'secret_day': 0,
        'secret_month': 0,
        'event': 0,
        'attempts': 0,
        'total_games': 0,
        'wins': 0,
        'bot_messages_ids':[],
        'user_messages_ids':[]
             }

# Словарь, в котором будут храниться данные пользователей
users = {}
def read_users_data():
    try:
        with sq.connect(current_path+'/users.db') as con:
            con.row_factory = sq.Row
            cur = con.cursor()
            cur.execute("""
            SELECT * from users
            """)
            records = cur.fetchall()
            for row in records:
                row = dict(row)
                print('dict row',row)
                user = row['user_id']
                users[user] = user_dict
                users[user]['in_game']= row['in_game']
                users[user]['secret_day']= row['secret_day']
                users[user]['secret_month']= row['secret_month']
                users[user]['event']= row['event']
                users[user]['attempts']= row['attempts']
                users[user]['total_games']= row['total_games']
                users[user]['wins']= row['wins']
            print('Чтение базы данных успешно завершено')
    except:
        print('Ошибка чтения базы данных')


    # with open(current_path+'/users_data', 'rb') as input_file:
    #     data_load = pickle.load(input_file)
    #     return data_load
def update_users_data(user):
    try:
        with sq.connect(current_path + '/users.db') as con:
            cur = con.cursor()

        # Обновить данные всех пользователей

            cur.execute("""
                        UPDATE users
                        SET in_game = ?,
                        secret_day = ?,
                        secret_month = ?,
                        event = ?,
                        attempts = ?,
                        total_games = ?,
                        wins = ?
                        WHERE user_id IS ?
                    """,
                        [users[user]['in_game'],
                         users[user]['secret_day'],
                         users[user]['secret_month'],
                         users[user]['event'],
                         users[user]['attempts'],
                         users[user]['total_games'],
                         users[user]['wins'],
                         user]
                        )
        print('Обновление базы данных успешно завершено',user,users[user])
    except:
        print('Ошибка обновления базы данных', user, users[user])

def write_users_data(user):
    try:
        with sq.connect(current_path+'/users.db') as con:
            cur = con.cursor()

            #Создать таблицу в случае отсутствия
            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER,
                in_game INTEGER,
                secret_day INTEGER,
                secret_month TEXT,
                event TEXT,
                attempts INTEGER,
                total_games INTEGER,
                wins INTEGER
            )""")

            #Добавить пользователя в БД в случае отсутствия
            cur.execute("""INSERT OR REPLACE INTO users(
                        user_id ,
                        in_game ,
                        secret_day ,
                        secret_month ,
                        event ,
                        attempts ,
                        total_games ,
                        wins 
                    )
                    VALUES
                    (?,?,?,?,?,?,?,?)
                    
                    """,
                        [user,
                         users[user]['in_game'],
                         users[user]['secret_day'],
                         users[user]['secret_month'],
                         users[user]['event'],
                         users[user]['attempts'],
                         users[user]['total_games'],
                         users[user]['wins']]
                        )
        print('Запись в базу данных успешно завершена')
    except:
        print('Ошибка записи в базу данных')
    # {users[user]['in_game']},{users[user]['secret_day']},{users[user]['secret_month']},{users[user]['event']},{users[user]['attempts']},{users[user]['total_games']},{users[user]['wins']},{users[user]}
    # with open(current_path+'/users_data', 'wb') as output_file:
    #     pickle.dump(users,output_file)




# users:dict = read_users_data()


# for user in users:
#     users[user]['bot_messages_ids'] = []
#     users[user]['user_messages_ids'] = []
#
# if __name__ == '__main__':
#     write_users_data()
#     read_users_data()
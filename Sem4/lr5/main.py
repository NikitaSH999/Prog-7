import sqlite3


def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def wrapper(func):
    file = open('file.txt', 'r')
    f = file.read()
    my_user = f.split(', ')
    login = str(my_user[0]) # получение логина
    password = str(my_user[1]) # и пароля
    
    def inner():
        # подключение к БД
        conn_dict = connect_to_db('example.db')
        conn, cur = conn_dict["conn"], conn_dict["cursor"]
        table = 'users'
        users = get_users_from_table(conn, table)
        
        try:
            # получение пользователя из БД и проверка правильности пароля
            sql_query = "SELECT login, pass FROM " + table + " WHERE login = " + login + " AND pass = " + password
            res = cur.execute(sql_query)
            user = res.fetchall()
        except:
            user = None
        # аутентификация
        if user is not None:
            print('Найденный пользователь: ' + str(user))
            return func()
        else:
            print('Пользователя с таким логином и паролем не существует, или вы ввели неверный логин или пароль.')
            print('Регистрация новых пользователей пока не доступна.')
            return None
    
    file.close()
    return inner

@wrapper
def private_zone_area():
    print('private zone area')
    return "private_zone_area"

def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()

    return users_lst


conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

try:
    sql_query = '''CREATE TABLE users
             (login text, pass text, role int)'''
    cur.execute(sql_query)
except sqlite3.OperationalError as e:
    e_str = str(e)

    if ("already exists" in e_str):
        print(f' NOTICE: {e}. CONTINUE ')

else:
  sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''
  users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe', 2)]
  try:
    cur.executemany(sql_query, users_lst)
    conn.commit()
  except sqlite3.Error as e:
    print(f'Error with adding users to db. {e}')

table = 'users'
users = get_users_from_table(conn, table)            

print(users)

print('\n')
private_zone_area()

conn.close()
cur, conn = None, None

import sqlite3

# Рефакторинг добавления данных (insert_param_data)
# Добавить код, который реализует: 
# параметризованное удаление данных (DELETE),
# обновление (изменение) данных (UPDATE), 
# выборку (извлечение) данных из таблицы stocks (SELECT)
# Добавить обработку исключительных ситуаций

def connect_to_db(path_to_db):

    connection = None
    if (path_to_db):
        try:
            # connection = sqlite3.connect(
                # 'file:' + path_to_db + '?mode=rw', uri=True)
            connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


# TODO
def create_table(table_name, domens_lst, conn):
    # проверяем есть ли conn
    # если нет, падаем / возвращаем None
    # если есть соединение, проверить есть ли таблица, если есть, то все ок и создавать не надо
    # если нет, то создадим и вернем какой-то код, если все хорошо
    pass

def delete_table(conn, table_name, values):
    c = conn.cursor()
    c.executemany(f'DELETE VALUES (?, ?, ?, ?, ?) FROM stocks', values)
    conn.commit()
    
def update_table(conn, table_name, values):
    c = conn.cursor()
    c.executemany(f'UPDATE stocks SET VALUES = (?) WHERE VALUES = (?)', values[0], values[1])
    conn.commit()

def insert_param_data(conn, table_name, values):
    # date text, trans text, symbol text, qty real, price real
    c = conn.cursor()
    c.executemany(f'INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', values)
    conn.commit()



conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')
except sqlite3.Error as e:
    print(f'table stocks already exists')
    pass

values = [('2020-02-20', 'HAS', 'APL', 100, 42.00)]

insert_param_data(conn, 'stocks', values)

for record in cur.execute("SELECT * FROM stocks"):
    print(record)
    
values = [('2020-02-20', 'BUY', 'APL', 100, 42.00)]

update_table(conn, 'stocks', values)

for record in cur.execute("SELECT * FROM stocks"):
    print(record)

conn.close()
conn, cur = None, None

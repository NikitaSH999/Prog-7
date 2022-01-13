import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

con.execute(
    'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)'
)
con.commit()

values = []
while True:
    print('For EXIT press Enter (send empty string)')
    name = input('Enter name: ')
    if name == "":
        break
    email = input('Enter email: ')
    if email == "":
        break
    values.append([name,email])

for i in range(len(values)):
    cur.execute('INSERT INTO users (name, email) VALUES (?,?)', values[i])
    con.commit()

cur.execute('SELECT * FROM users')
print(cur.fetchall())

con.close()
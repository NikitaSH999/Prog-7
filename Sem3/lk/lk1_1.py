import sqlite3
conn=sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real) ''')
except sqlite3.OperationalError:
	print('Table already exists. Continue...')

c.execute("INSERT INTO stocks VALUES ('2006-10-06','BUY','RTAH',100,35.14)")

conn.commit()

for record in c.execute("SELECT * FROM stocks"):
	print (record)

conn.close()


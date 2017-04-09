import sqlite3

conn = sqlite3.connect('sqlitetest.db')
c = conn.cursor()

c.execute(''' SELECT * FROM EventLog ''')


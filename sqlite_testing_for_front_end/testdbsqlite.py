import sqlite3

conn = sqlite3.connect('sqlitetest.db')
c = conn.cursor()

c.execute('''
	CREATE TABLE EventLog (
		EventID 	INTEGER 		NOT NULL PRIMARY KEY AUTOINCREMENT,
		Event 		VARCHAR(512) 	NOT NULL,
		Vegetable 	VARCHAR(128) 	NOT NULL,
		Timelog 	DATETIME 		NOT NULL,
		Planter 	INT 			NOT NULL
	);
''')

conn.commit()
conn.close()
#create a connection to MySQL
connection = MySQLdb.connect(host = "localhost", user = "root", passwd='toor', db = "harvester"	 )
#create cursor object whcih lets us interact with the database
cursor = connection.cursor()

cursor.execute('INSERT INTO plant (type, scientific_name, description) VALUES (%s, %s, %s)' %  ('Beef Tomato', 'Solanum lycopersicum', 'a big tomato'))
cursor.execute('INSERT INTO plant (type, scientific_name, description) VALUES (%s, %s, %s)' %  ('Potato', 'Solanum tuberosum', 'turn into french fries'))
cursor.execute('INSERT INTO plant (type, scientific_name, description) VALUES (%s, %s, %s)' %  ('Eggplant', 'Solanum melongena', 'for making eggplant food'))
cursor.execute('INSERT INTO plant (type, scientific_name, description) VALUES (%s, %s, %s)' %  ('Spearmint', 'Mentha', 'for making gum'))
cursor.execute('INSERT INTO plant (type, scientific_name, description) VALUES (%s, %s, %s)' %  ('Pepper', 'Piper nigrum', 'mexican food'))

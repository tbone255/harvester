import MySQLdb

#create a connection to MySQL
connection = MySQLdb.connect(host = "localhost", user = "root", db = "harvester"	 )
#create cursor object whcih lets us interact with the database
cursor = connection.cursor()

cursor.execute(''' INSERT INTO plant (type, scientific_name, description) VALUES ("%s", "%s", "%s") ''' 
				%  ("Beef Tomato", "Solanum lycopersicum", "a big tomato"))

cursor.execute(''' INSERT INTO plant (type, scientific_name, description) VALUES ("%s", "%s", "%s") '''
				%  ('Potato', 'Solanum tuberosum', 'turn into french fries'))

cursor.execute(''' INSERT INTO plant (type, scientific_name, description) VALUES ("%s", "%s", "%s") '''
				%  ('Eggplant', 'Solanum melongena', 'for making eggplant food'))

cursor.execute(''' INSERT INTO plant (type, scientific_name, description) VALUES ("%s", "%s", "%s") '''
				%  ('Spearmint', 'Mentha', 'for making gum'))

cursor.execute(''' INSERT INTO plant (type, scientific_name, description) VALUES ("%s", "%s", "%s") '''
				%  ('Pepper', 'Piper nigrum', 'mexican food'))



cursor.execute(''' INSERT INTO planter (length, width) VALUES (%s, %s) ''' 
				%  (60, 48))

cursor.execute(''' INSERT INTO planter (length, width) VALUES (%s, %s) ''' 
				%  (48, 48))

cursor.execute(''' INSERT INTO planter (length, width) VALUES (%s, %s) ''' 
				%  (48, 48))

cursor.execute(''' INSERT INTO planter (length, width) VALUES (%s, %s) ''' 
				%  (60, 60))



cursor.execute(''' INSERT INTO event (event_type, description) VALUES ("%s", "%s") '''
				% ("Harvest", "Harvested peppers"))

cursor.execute(''' INSERT INTO event (event_type, description) VALUES ("%s", "%s") '''
				% ("Water", "Give plants water"))

cursor.execute(''' INSERT INTO event (event_type, description) VALUES ("%s", "%s") '''
				% ("Feed", "Give plants food"))

cursor.execute(''' INSERT INTO event (event_type, description) VALUES ("%s", "%s") '''
				% ("Tornado", "Tornado ravaged lands, greenhouse is lost"))

cursor.execute(''' INSERT INTO event (event_type, description) VALUES ("%s", "%s") '''
				% ("Shit", "Shit in the compost"))


cursor.execute(''' INSERT INTO nutrition (brand, type, description) VALUES ("%s", "%s", "%s") '''
				% ("Peat", "0-11-11", "Good for tomatoes"))

cursor.execute(''' INSERT INTO nutrition (brand, type, description) VALUES ("%s", "%s", "%s") '''
				% ("Buddy's", "8-8-8", "Crop fertilizer"))



cursor.execute(''' INSERT INTO event_log (event_id, plant_id, planter_id, timestamp, description) VALUES ("%s", "%s", "%s", "%s", "%s") '''
				% ("11", "11", "9", "2017-04-01 10:00:00", "harvested 10oz peppers"))

cursor.execute(''' INSERT INTO event_log (event_id, plant_id, planter_id, timestamp, description) VALUES ("%s", "%s", "%s", "%s", "%s") '''
				% ("12", "12", "10", "2017-04-02 1:30:00", "watered plants"))

#
#cursor.execute(''' INSERT INTO event_log (event_id, plant_id, planter_id, nutrition_id, tstamp, description) VALUES (%s, %s, %s, %s, %s, %s) '''
#				% ("13", "13", "11", "", "", ""))
#
#cursor.execute(''' INSERT INTO event_log (event_id, plant_id, planter_id, nutrition_id, tstamp, description) VALUES (%s, %s, %s, %s, %s, %s) '''
#				% ("14", "14", "9", "", "", ""))
#
#cursor.execute(''' INSERT INTO event_log (event_id, plant_id, planter_id, nutrition_id, tstamp, description) VALUES (%s, %s, %s, %s, %s, %s) '''
#				% ("15", "15", "9", "", "", ""))
#
connection.commit()
connection.close()

















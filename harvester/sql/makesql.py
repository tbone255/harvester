import MySQLdb

#create a connection to MySQL
connection = MySQLdb.connect(host = "localhost", user = "root", passwd='toor', db = "harvester"	 )
#create cursor object whcih lets us interact with the database
cursor = connection.cursor()

#create the main table that shows event, veg, the date, which planter
#create table for tracking harvests, associated with the eventid from main table, how many u harvest
#create table for tracking plant events
cursor.execute('''

	CREATE TABLE `plant` (
		`plant_id`			INTEGER			NOT NULL AUTO_INCREMENT,
		`type`				VARCHAR(32)		NOT NULL,
		`scientific_name`	VARCHAR(128)	NOT NULL,
		`description`		VARCHAR(512)	NOT NULL,
		PRIMARY KEY (`plant_id`)
	) ENGINE=InnoDB;

	CREATE TABLE `event` (
		`event_id`			INTEGER			NOT NULL AUTO_INCREMENT,
		`event_type`		VARCHAR(32)		NOT NULL,
		PRIMARY KEY (`event_id`)
	) ENGINE=InnoDB;

	CREATE TABLE `nutrition` (
		`nutrition_id`		INTEGER			NOT NULL AUTO_INCREMENT,
		`brand`				VARCHAR(32)		DEFAULT NULL,
		`type`				VARCHAR(32)		NOT NULL,
		`description`		VARCHAR(128)	NOT NULL,
		PRIMARY KEY (`nutrition_id`)
	) ENGINE=InnoDB;

	CREATE TABLE `event_log` (
		`event_log_id`		INTEGER			NOT NULL AUTO_INCREMENT,
		`event_id`			INTEGER			NOT NULL,
		`plant_id`			INTEGER,
		`planter_id`		INTEGER,
		`nutrition_id`		INTEGER			DEFAULT NULL,
		`timestamp`			DATETIME		DEFAULT NULL,
		`description`		VARCHAR(256),
		PRIMARY KEY (`event_log_id`)
	) ENGINE=InnoDB;

''')

#close the connection
cursor.close()

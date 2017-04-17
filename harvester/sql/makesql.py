import MySQLdb

#create a connection to MySQL
connection = MySQLdb.connect(host = "localhost", user = "root", passwd='toor', db = "harvester"	 )
#create cursor object whcih lets us interact with the database
cursor = connection.cursor()

#create the main table that shows event, veg, the date, which planter
#create table for tracking harvests, associated with the eventid from main table, how many u harvest
#create table for tracking plant events
cursor.execute('''

	CREATE TABLE EventLog (
		EventID 	INT 			NOT NULL AUTO_INCREMENT,
		Event 		VARCHAR(512) 	NOT NULL,
		Vegetable	VARCHAR(128)	NOT NULL,
		Timelog		DATETIME		NOT NULL,
		Planter		INT   			NOT NULL,
		PRIMARY KEY (EventID)
	);

	CREATE TABLE Harvest (
		HarvestID	INT 			NOT NULL AUTO_INCREMENT,
		EventID		INT 			NOT NULL,
		Amount 		INT 			NOT NULL,
		Description VARCHAR(256),
		PRIMARY KEY (HarvestID),
		FOREIGN KEY (EventID) 		REFERENCES EventLog(EventID)
	);

	CREATE TABLE Planting (
		PlantID		INT 			NOT NULL AUTO_INCREMENT,
		EventID		INT 			NOT NULL,
		Amount 		INT 			NOT NULL,
		Description VARCHAR(256),
		PRIMARY KEY (PlantID),
		FOREIGN KEY (EventID) 		REFERENCES EventLog(EventID)
	);

	CREATE TABLE Nutrition (
		NutritionID INT 			NOT NULL AUTO_INCREMENT,
		EventID 	INT 			NOT NULL,
		Water 		BOOLEAN,
		Fertilizer 	VARCHAR(256),
		PRIMARY KEY (NutritionID),
		FOREIGN KEY (EventID) 		REFERENCES EventLog(EventID)
	);

''')

#close the connection
cursor.close()

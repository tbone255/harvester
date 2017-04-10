import MySQLdb

connection = MySQLdb.connect(host = "localhost", user = "root", db = "harvester")
cursor = connection.cursor()

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
		HarvestID	INT 	NOT NULL AUTO_INCREMENT,
		EventID		INT 	NOT NULL,
		Amount 		INT 	NOT NULL,
		PRIMARY KEY (HarvestID),
		FOREIGN KEY (EventID) REFERENCES EventLog(EventID)
	);

	CREATE TABLE Nutrition (
		NutritionID INT 	NOT NULL AUTO_INCREMENT,
		EventID 	INT 	NOT NULL,
		Water 		BOOLEAN,
		Fertilizer 	VARCHAR(256),
		PRIMARY KEY (NutritionID),
		FOREIGN KEY (EventID) REFERENCES EventLog(EventID)
	);

	''')

cursor.close()

# A simple program that creates connection to database
# and lists the tables
import argparse
import sys

from sqlalchemy import create_engine

class DB(object):
    def __init__(self, db_uri=None):
        self.engine = create_engine(db_uri) #sets up uri

    def get_connection(self):
        return self.engine.connect() #connects to server

    def get_tables(self):
        conn = self.get_connection()
        result = conn.execute('show tables;') #retrieves tables
        return result #returns tables

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MySQL Database test') #parser setup
    parser.add_argument('--db_uri', type=str, dest='db', #--db_uri for mysql uri in cli
        help='Database uri')
    args = parser.parse_args()

    if not args.db:
        sys.exit('You must provide a db uri')

    database = DB(args.db)
    result = database.get_tables() #gets tables and puts it in result
    for table in result: #loops through and prints out table names
        print table

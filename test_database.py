# A simple program that creates connection to database
# and lists the tables
import argparse
import sys

from sqlalchemy import create_engine

class DB(object):
    def __init__(self, db_uri=None):
        self.engine = create_engine(db_uri)

    def get_connection(self):
        return self.engine.connect()

    def get_tables(self):
        conn = self.get_connection()
        result = conn.execute('show tables;')
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MySQL Database test')
    parser.add_argument('--db_uri', type=str, dest='db',
        help='Database uri')
    args = parser.parse_args()

    if not args.db:
        sys.exit('You must provide a db uri')

    database = DB(args.db)
    result = database.get_tables()
    for row in result:
        print row

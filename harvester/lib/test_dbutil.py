import argparse
import sys
import pprint

from dbutil import DBUtil 


def main():
    dbutil = DBUtil(args.db)

    result = dbutil.get_nutrition_for_plant(1)
    pprint.pprint(result)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MySQL Database test')
    parser.add_argument('--db_uri', type=str, dest='db',
        help='Database uri')
    args = parser.parse_args()

    if not args.db:
        sys.exit('You must provide a db uri')

    main()
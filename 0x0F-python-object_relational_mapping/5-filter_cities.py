#!/usr/bin/python3
""" Lists all cities from a name of a state"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            JOIN states ON states.id = cities.state_id\
            WHERE states.name = '{}'\
            ORDER BY cities.id".format(state_name))
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()

#!/usr/bin/python3
""" Lists all cities from hbtn_0e_0_usa"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON state_id = states.id ORDER BY cities.id")
rows = cur.fetchall()

for row in rows:
    print(row)
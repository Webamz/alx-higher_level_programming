#!/usr/bin/python3
""" Lists states with name starting with N"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)
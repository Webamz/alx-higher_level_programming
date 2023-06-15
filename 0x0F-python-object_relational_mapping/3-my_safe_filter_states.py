#!/usr/bin/python3
""" Displays states that match the name argument"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE states.name=%s ORDER BY states.id ASC", (state_name,))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
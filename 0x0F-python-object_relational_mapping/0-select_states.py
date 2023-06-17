#!/usr/bin/python3
""" lists all states from database hbtn_0e_o_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=usr,\
                     passwd=password, db=database) 
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
            ORDER BY states.id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)
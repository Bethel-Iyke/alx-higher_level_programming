#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.

"""
import sys
from sys import argv
import MySQLdb

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], port=3306,
            db=sys.argv[3], charset="utf8")
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name \
LIKE %s ORDER BY id ASC", (argv[4],))
rows = cur.fetchall()
for row in rows:
print(row)

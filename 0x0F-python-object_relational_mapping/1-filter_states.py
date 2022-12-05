#!/usr/bin/python3
"""
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.

"""
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                     passwd=sys.argv[2], port=3306, db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM `states` ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
if row[1][0] == "N":
print(row)

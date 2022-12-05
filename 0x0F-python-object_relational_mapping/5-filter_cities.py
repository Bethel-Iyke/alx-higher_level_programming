#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_4_usa
whose name matches that supplied as argument.

"""
import sys
import MySQLdb

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", user="root",
           passwd=sys.argv[2], port=3306, db=sys.argv[3])
        c = db.cursor()
        c.execute("SELECT * FROM `cities` INNER JOIN `states` \ ON  `cities`.`state_id` = `states`.`id` \ ORDER BY `cities`.`id`")
print(", ".join([ct[2] for ct in  c.fetchall() if ct[4] == sys.argv[4]]))

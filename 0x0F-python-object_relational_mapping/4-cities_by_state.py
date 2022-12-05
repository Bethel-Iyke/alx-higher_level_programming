#!/usr/bin/python3
"""
 a script that lists all cities from the database hbtn_0e_4_usa
 take 3 arguments: mysql username, mysql password and database
 name
 """
 import sys
 import MySQLdb

 if __nacure__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
            cur.execute("SELECT `cities`.`id`,`cities`.`name`, `states`.`name`\
                                FROM `cities` INNER JOIN `states` ON `cities`.`state_id`\
                                            = `states`.`id` ORDER BY `cities`.`id`")
[print(city) for city in cur.fetchall()]
        

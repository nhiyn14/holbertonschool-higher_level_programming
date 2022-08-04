#!/usr/bin/python3
"""
lists all cities of that state taking from argument
 from the database hbtn_0e_4_usa, including:
table states (states.id, states.name)
table cities (cities.name, cities.id, cities.state_id -> states.id)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name LIKE %s\
                ORDER BY cities.id ASC", (argv[4],))
    cities = cur.fetchall()
    print(', '.join(city[0] for city in cities))
    cur.close()
    db.close()

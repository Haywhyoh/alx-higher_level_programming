#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON state.id = cities.state_id\
        ORDER BY states.id ASC')
    for state in cur.fetchall():
        print(state)

    db.close()

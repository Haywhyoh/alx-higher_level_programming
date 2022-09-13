#!/usr/bin/python3
"""
List all cities of a state
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.states_id = states.id WHERE states.name = '{}';".format(argv[4]))
    states = cur.fetchall()
    print(", ".join([state[1] for state in states]))
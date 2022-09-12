#!/usr/bin/python3
"""
lists all states from database hbtn_0e_0_usa starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELCET * FROM states WHERE name = '{%s}' ORDER BY id".format(sys.argv[4]))

    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)

    db.close()
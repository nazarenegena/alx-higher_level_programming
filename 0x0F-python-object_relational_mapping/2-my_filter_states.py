#!/usr/bin/python3
""" listthe state that matches user input
from database hbtn_0e_0_usa using MySQLdb """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    search_term = sys.argv[4]
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE
                   '{}' ORDER BY states.id".format(search_term))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()

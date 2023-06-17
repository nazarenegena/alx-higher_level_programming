#!/usr/bin/python3
""" list the state that matches user input """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    search_term = sys.argv[4]
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (search_term, ))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()

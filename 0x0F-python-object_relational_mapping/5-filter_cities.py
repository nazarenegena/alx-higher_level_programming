#!/usr/bin/python3
""" list all cities by state from database hbtn_0e_0_usa using MySQLdb """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    cities = cursor.fetchall()
    city = list(city[0] for city in cities)
    print(*city, sep=", ")
    cursor.close()
    database.close()

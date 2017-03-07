import string
import random
import mysql.connector
import pymysql.cursors
from model.group_address import Address_data


#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)
#finally:
#    connection.close()


def test_2(app, db):
    x = db.get_contact_list()
    print(x)

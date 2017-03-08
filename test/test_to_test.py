import string
import random
import mysql.connector
import pymysql.cursors
from model.group_address import Address_data
from fixture.orm import ORMFixture
from model.group import Group



db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_not_in_groups(Group(id="208"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass



#def test_2(app, db):
#    x = db.get_contact_list()
#    print(x)



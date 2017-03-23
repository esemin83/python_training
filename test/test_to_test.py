import string
import random
import mysql.connector
import pymysql.cursors
from model.group_address import Address_data
from fixture.orm import ORMFixture
from model.group import Group


'''
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_not_in_groups(Group(id="208"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
'''

'''
def test_2(app, orm):
    group_list = orm.get_group_list()
    group_random = random.choice(group_list)
    x = orm.get_contact_in_groups(group_random)
    print(x)


def test_3(app, orm):
    group_list = orm.get_group_list()
    group_random = random.choice(group_list)
    y = orm.get_contact_not_in_groups(group_random)
    print("y =", y)
'''


def test_add_contact_to_group_contact_not_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))
    if len(orm.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))

    group_list = orm.get_group_list()
    group_to_add = random.choice(group_list)

    if len(orm.get_contact_not_in_groups(group_to_add)) != 0:
        x = orm.get_contact_not_in_groups(group_to_add)
        contact_to_add = random.choice(x)
        app.group.add_contact_to_group_v01(contact_to_add.id, group_to_add.id)
        assert orm.get_contact_in_groups(group_to_add).index(contact_to_add) is not None
    else:
        contact_to_add = Address_data(firstname="FIRSTNAME", middlename="D", lastname="LASTNAME", nickname="RR",
                                      company="USA", address="Texas")
        app.group.add_new_address_form(contact_to_add)
        contact_list = orm.get_contact_list()
        contact_id = sorted(contact_list, key=Address_data.id_or_max)[-1].id
        contact_list.remove(sorted(contact_list, key=Address_data.id_or_max)[-1])
        contact_list.append(Address_data(id=contact_id, firstname=contact_to_add.firstname,
                                         middlename=contact_to_add.middlename, lastname=contact_to_add.lastname,
                                         nickname=contact_to_add.nickname, company=contact_to_add.company,
                                         address=contact_to_add.address))
        added_contact = sorted(contact_list, key=Address_data.id_or_max)[-1]
        app.group.add_contact_to_group_v01(contact_id, group_to_add.id)
        assert orm.get_contact_in_groups(group_to_add).index(added_contact) is not None

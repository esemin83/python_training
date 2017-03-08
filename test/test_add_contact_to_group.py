from model.group_address import Address_data
import random
from fixture.orm import *
from random import randrange


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name_1"))
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    contact_to_add = random.choice(contact_list)
    group_to_add_number = randrange(len(group_list))
    group_to_add = group_list[group_to_add_number]
    app.group.add_contact_to_group(contact_to_add.id, group_to_add_number)
    x = orm.get_contact_in_groups(group_to_add)
    y = []
    y.append(contact_to_add)
    assert x == y
    #print(len(x))
    #assert db.get_contact_in_groups




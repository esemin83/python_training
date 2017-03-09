import random
#from fixture.orm import *
from model.group import Group
from model.group_address import Address_data


#def test_add_contact_to_group_1(app, db, orm):
#    app.group.add_contact_to_group_v01("445", "257")


def test_add_contact_to_group_orm(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))

    contact_list = orm.get_contact_list()
    contact_to_add = random.choice(contact_list)

    group_list = orm.get_group_list()
    group_to_add = random.choice(group_list)

    app.group.add_contact_to_group_v01(contact_to_add.id, group_to_add.id)

    added_contact = []
    added_contact.append(contact_to_add)

    assert orm.get_contact_in_groups(group_to_add) == added_contact


#def test_add_contact_to_group_1(app, db, orm):
#    app.group.add_contact_to_group_v01("445", "257")









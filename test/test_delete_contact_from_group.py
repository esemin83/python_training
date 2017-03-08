import random
from random import randrange
from model.group_address import Address_data
from model.group import Group


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))

    group_list = db.get_group_list()
    group_to_add_number = randrange(len(group_list))
    group_to_del = group_list[group_to_add_number]

    contact_list = db.get_contact_list()
    contact_to_add = random.choice(contact_list)

    x = orm.get_contact_in_groups(group_to_del)
    if len(orm.get_contact_in_groups(group_to_del)) == 0:
        app.group.add_contact_to_group(contact_to_add.id, group_to_add_number)
    app.group.delete_contact_from_group(contact_to_add.id,  group_to_add_number)




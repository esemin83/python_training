import random
#from fixture.orm import *
from model.group import Group
from model.group_address import Address_data


def test_add_contact_to_group_orm(app, orm):
    added_contact = []
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
    added_contact.append(contact_to_add)
    assert orm.get_contact_in_groups(group_to_add).index(contact_to_add) is not None


def test_add_contact_to_group_contact_not_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))
    if len(orm.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))

    group_list = orm.get_group_list()
    group_to_add = random.choice(group_list)

    if len(orm.get_contact_not_in_groups(group_to_add)) != 0:
        list = orm.get_contact_not_in_groups(group_to_add)
        contact_to_add = random.choice(list)
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










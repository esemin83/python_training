import random
from model.group import Group
from model.group_address import Address_data


def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))

    contact_list = orm.get_contact_list()
    contact_to_del = random.choice(contact_list)

    group_list = orm.get_group_list()
    group_to_del = random.choice(group_list)

    if len(orm.get_contact_in_groups(group_to_del)) == 0:
        app.group.add_contact_to_group_v01(contact_to_del.id, group_to_del.id)

    app.group.delete_contact_from_group(contact_to_del.id, group_to_del.id)

    #deleted_from_group_contact = []
    #deleted_from_group_contact.append(contact_to_del)

    y = orm.get_contact_not_in_groups(group_to_del).index(contact_to_del)
    print(y)

    #assert orm.get_contact_not_in_groups(group_to_del).index(contact_to_del)
    #assert orm.get_contact_not_in_groups(group_to_del).index(deleted_from_group_contact)
    assert orm.get_contact_not_in_groups(group_to_del).index(contact_to_del) is not None





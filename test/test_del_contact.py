from model.group_address import Address_data
from random import randrange


def test_del_contact(app):
    if app.group.count_contact() == 0:
        app.group.add_new_address_form(Address_data(firstname="for_delete", middlename="for_delete",
                                                    lastname="for_delete", nickname="for_delete",
                                                    company="for_delete", address="for_delete"))
    old_contacts = app.group.get_contact_rows()
    index = randrange(len(old_contacts))
    app.group.delete_some_contact(index)
    assert len(old_contacts) - 1 == app.group.count_contact()
    new__contacts = app.group.get_contact_rows()
    old_contacts[index:index+1] = []
    assert old_contacts == new__contacts

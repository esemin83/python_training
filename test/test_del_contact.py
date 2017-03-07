from model.group_address import Address_data
from random import randrange
import random
from test.test_string_value import merge_emails
from test.test_string_value import merge_phones_like_on_homepage


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


def test_del_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="for_delete", middlename="for_delete",
                                                    lastname="for_delete", nickname="for_delete",
                                                    company="for_delete", address="for_delete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.group.delete_some_contact_by_id(contact.id)
    new__contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new__contacts)
    old_contacts.remove(contact)
    assert old_contacts == new__contacts
    if check_ui:
        def clean(address_data):
            return Address_data(id=address_data.id, firstname=address_data.firstname, lastname=address_data.lastname,
                                address=address_data.address.strip(),
                                all_phone_from_home_page=merge_phones_like_on_homepage(address_data),
                                all_emails=merge_emails(address_data))
        assert sorted(map(clean, new__contacts), key=Address_data.id_or_max) == sorted(app.group.get_contact_rows(), key=Address_data.id_or_max)

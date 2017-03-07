# -*- coding: utf-8 -*-
from model.group_address import Address_data
#import pytest
#from data.contacts import testdata
#from data.add_contact import constant as testdata
from test.test_string_value import merge_emails
from test.test_string_value import merge_phones_like_on_homepage


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_list = app.group.get_contact_rows()
    app.group.add_new_address_form(contact)
    assert len(old_list) + 1 == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)


def test_add_contact_db(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_list = db.get_contact_list()
    app.group.add_new_address_form(contact)
    #assert len(old_list) + 1 == app.group.count_contact()
    new_list = db.get_contact_list()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)
    if check_ui:
        def clean(address_data):
            return Address_data(id=address_data.id, firstname=address_data.firstname, lastname=address_data.lastname,
                                address=address_data.address.strip(),
                                all_phone_from_home_page=merge_phones_like_on_homepage(address_data),
                                all_emails=merge_emails(address_data))
        assert sorted(map(clean, new_list), key=Address_data.id_or_max) == sorted(app.group.get_contact_rows(), key=Address_data.id_or_max)
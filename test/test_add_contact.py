# -*- coding: utf-8 -*-
from model.group_address import Address_data
#import pytest
#from data.contacts import testdata
#from data.add_contact import constant as testdata


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_list = app.group.get_contact_rows()
    app.group.add_new_address_form(contact)
    assert len(old_list) + 1 == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
#def test_add_contact(app, data_contacts):
#    contact = data_contacts
#    old_list = app.group.get_contact_rows()
#    app.group.add_new_address_form(contact)
#    assert len(old_list) + 1 == app.group.count_contact()
#    new_list = app.group.get_contact_rows()
#    old_list.append(contact)
#    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)


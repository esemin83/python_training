from model.group_address import Address_data


def test_del_contact(app):
    if app.group.count_contact() == 0:
        app.group.add_new_address_form(Address_data(firstname="for delete", middlename="for delete",
                                                    lastname="for delete", nickname="for delete",
                                                    company="for delete", address="for delete"))
    old_contacts = app.group.get_contact_rows()
    app.group.delete_first_contact()
    new_contacts = app.group.get_contact_rows()
    assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[0:1] = []
    assert old_contacts == new_contacts

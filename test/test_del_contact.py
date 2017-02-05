from model.group_address import Address_data


def test_del_contact(app):
    if app.group.count_contact() == 0:
        app.group.add_new_address_form(Address_data(firstname="for delete", middlename="for delete",
                                                    lastname="for delete", nickname="for delete",
                                                    company="for delete", address="for delete"))
    app.group.delete_first_contact()


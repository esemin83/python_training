# -*- coding: utf-8 -*-
from model.group_address import Address_data


def test_add_contact(app):
    old_list = app.group.get_contact_rows()
    contact = (Address_data(firstname="Jonny", middlename="Q", lastname="Cage", nickname="JQ",
                            company="Andromeda", address="Moskow", home_phone="455-63-63",
                            mobile_phone="+7-000-000-00-00", work_phone="456-85-85",
                            email_1="fake_1@mail.ru", email_2="fake_2@mail.ru",
                            home_page="www.page.ru"))
    app.group.add_new_address_form(contact)
    new_list = app.group.get_contact_rows()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(contact)
    #print(sorted(new_list, key=Address_data.id_or_max))
    #print(sorted(new_list, key=Address_data.id_or_max))
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)

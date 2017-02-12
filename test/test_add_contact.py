# -*- coding: utf-8 -*-
from model.group_address import Address_data


def test_add_contact(app):
    #old_contacts = app.group.get_contact_list()
    app.group.add_new_address_form(Address_data(firstname="Jonny", middlename="Q", lastname="Cage", nickname="JQ",
                                                company="Andromeda", address="Moskow", home_phone="455-63-63",
                                                mobile_phone="+7-000-000-00-00", work_phone="456-85-85",
                                                email_1="fake_1@mail.ru", email_2="fake_2@mail.ru",
                                                home_page="www.page.ru"))
    #new_contacts = app.group.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)


#def test_add_chuck_contact(app):
#    app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
#                                                company="USA", address="Texas"))

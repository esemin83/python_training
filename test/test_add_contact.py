# -*- coding: utf-8 -*-
from model.group_address import Address_data


def test_add_contact(app):
    old_list = app.group.get_contact_rows()
    contact = (Address_data(firstname="Jonny", middlename="Q", lastname="Cage", nickname="JQ",
                            company="Andromeda", address="Moskow", home_phone="(455)6363",
                            mobile_phone="700-00000", work_phone="4568585",
                            fax_phone="065841", email_1="fake_1@mail.ru", email_2="fake_2@mail.ru",
                            home_page="www.page.ru"))
    app.group.add_new_address_form(contact)
    assert len(old_list) + 1 == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)


def test_add_contact_1(app):
    old_list = app.group.get_contact_rows()
    contact = (Address_data(firstname="Jax", middlename="R", lastname="Hill", nickname="QR",
                            company="Alabama", address="Atlanta", home_phone="(400)6363",
                            mobile_phone="700-00321", work_phone="4001111",
                            fax_phone="5566951", email_1="mail_1@mail.ru", email_2="mail_1@mail.ru",
                            home_page="www.page_for_page.ru"))
    app.group.add_new_address_form(contact)
    assert len(old_list) + 1 == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)

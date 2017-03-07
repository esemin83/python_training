from model.group_address import Address_data
from random import randrange
import random
from test.test_string_value import merge_emails
from test.test_string_value import merge_phones_like_on_homepage


def test_modify_contact(app):
    if app.group.count_contact() == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    old_list = app.group.get_contact_rows()
    contact = Address_data(firstname="Jonny", middlename="T", lastname="Tramp", nickname="DT",
                           company="Tramp Inc", address="New York", home_phone="002-22-74",
                           mobile_phone="+7-521-000-00-00", work_phone="400-00-00",
                           fax_phone="8885217", email_1="fake_3@mail.ru", email_2="fake_4@mail.ru",
                           home_page="www.page_new.ru")
    index = randrange(len(old_list))
    contact.id = old_list[index].id
    app.group.modify_some_contact(contact, index)
    assert len(old_list) == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list[index] = contact
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(old_list, key=Address_data.id_or_max)


def test_modify_contact_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    old_list = db.get_contact_list()
    contact = Address_data(firstname="Jonny", middlename="T", lastname="Tramp", nickname="DT",
                           company="Tramp Inc", address="New York", home_phone="002-22-74",
                           mobile_phone="+7-521-000-00-00", work_phone="400-00-00",
                           fax_phone="8885217", email_1="fake_3@mail.ru", email_2="fake_4@mail.ru",
                           home_page="www.page_new.ru")
    cont = random.choice(old_list)
    app.group.modify_some_contact_by_id(contact, cont.id)
    contact.id = cont.id
    new_list = db.get_contact_list()
    old_list.remove(cont)
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(old_list, key=Address_data.id_or_max)
    if check_ui:
        def clean(address_data):
            return Address_data(id=address_data.id, firstname=address_data.firstname, lastname=address_data.lastname,
                                address=address_data.address.strip(),
                                all_phone_from_home_page=merge_phones_like_on_homepage(address_data),
                                all_emails=merge_emails(address_data))
        assert sorted(map(clean, new_list), key=Address_data.id_or_max) == sorted(app.group.get_contact_rows(), key=Address_data.id_or_max)


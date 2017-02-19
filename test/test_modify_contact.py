from model.group_address import Address_data
from random import randrange


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
    print(len(old_list))
    contact.id = old_list[index].id
    app.group.modify_some_contact(contact, index)
    assert len(old_list) == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list[index] = contact
    #print(sorted(new_list, key=Address_data.id_or_max))
    #print(sorted(old_list, key=Address_data.id_or_max))
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(old_list, key=Address_data.id_or_max)


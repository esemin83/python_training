from model.group_address import Address_data


def test_modify_contact(app):
    app.group.modify_contact(Address_data(firstname="Donald", middlename="T", lastname="Tramp", nickname="DT",
                                          company="Tramp Inc", address="New York", home_phone="002-22-74",
                                          mobile_phone="+7-521-000-00-00", work_phone="400-00-00",
                                          email_1="fake_3@mail.ru", email_2="fake_4@mail.ru",
                                          home_page="www.page_new.ru"))


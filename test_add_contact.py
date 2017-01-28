# -*- coding: utf-8 -*-
import pytest
from group_address import Address_data
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
        app.login(login= "admin", password= "secret")
        app.add_new_address_form(Address_data(firstname="Jonny", middlename="Q", lastname="Cage", nickname="JQ", company="Andromeda", address="Moskow", home_phone="455-63-63",
                                  mobile_phone="+7-000-000-00-00", work_phone="456-85-85", email_1="fake_1@mail.ru", email_2="fake_2@mail.ru", home_page="www.page.ru"))
        app.logout()

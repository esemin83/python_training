# -*- coding: utf-8 -*-
from model.group_address import Address_data
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    numbers = string.digits + " "*2 + "(" + ")" + "-"
    return "".join([random.choice(numbers) for x in range(maxlen)])


def random_mail(domen, maxlen):
    value = string.ascii_letters + string.digits
    return "".join([random.choice(value) for x in range(random.randrange(maxlen))]) + domen


testdata = [
    Address_data(firstname=random_string("firstname", 20), middlename=random_string("", 1),
                 lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                 company=random_string("company", 20), address=random_string("address", 20),
                 home_phone=random_numbers(10), mobile_phone=random_numbers(10), work_phone=random_numbers(10),
                 fax_phone=random_numbers(10), email_1=random_mail("@mail.ru", 10), email_2=random_mail("@mail.ru", 10),
                 home_page=random_string("page", 10))
    for x in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    old_list = app.group.get_contact_rows()
    app.group.add_new_address_form(contact)
    assert len(old_list) + 1 == app.group.count_contact()
    new_list = app.group.get_contact_rows()
    old_list.append(contact)
    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)


#def test_add_contact_1(app):
#    old_list = app.group.get_contact_rows()
#    contact = (Address_data(firstname="Jax", middlename="R", lastname="Hill", nickname="QR",
#                            company="Alabama", address="Atlanta", home_phone="(400)6363",
#                            mobile_phone="700-00321", work_phone="4001111",
#                            fax_phone="5566951", email_1="mail_1@mail.ru", email_2="mail_1@mail.ru",
#                            home_page="www.page_for_page.ru"))
#    app.group.add_new_address_form(contact)
#    assert len(old_list) + 1 == app.group.count_contact()
#    new_list = app.group.get_contact_rows()
#    old_list.append(contact)
#    assert sorted(new_list, key=Address_data.id_or_max) == sorted(new_list, key=Address_data.id_or_max)

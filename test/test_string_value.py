import re


def test_string_value(app):
    data_from_homepage = app.group.get_contact_rows()[0]
    data_from_edit_page = app.group.get_contact_from_edit_page(0)
    # test names
    assert (clear(data_from_homepage.firstname) == clear(data_from_edit_page.firstname)) and \
           (clear(data_from_homepage.lastname) == clear(data_from_edit_page.lastname))
    # test emails
    assert clear(data_from_homepage.all_emails) == clear(merge_emails(data_from_edit_page))
    # test phones
    assert data_from_homepage.all_phone_from_home_page == merge_phones_like_on_homepage(data_from_edit_page)
    # test address
    assert clear(data_from_homepage.address) == clear(data_from_edit_page.address)


def merge_phones_like_on_homepage(address_data):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address_data.home_phone, address_data.mobile_phone, address_data.work_phone]))))


def merge_emails(address_data):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [address_data.email_1, address_data.email_2])))


def clear(s):
    return re.sub("[() -]", "", s)

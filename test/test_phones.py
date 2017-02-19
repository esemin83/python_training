import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.group.get_contact_rows()[0]
    contact_from_edit_page = app.group.get_contact_from_edit_page(0)
    #x = merge_phones_like_on_homepage(contact_from_edit_page)
    #y = contact_from_home_page.all_phone_from_home_page
    #print(x , y)
    assert contact_from_home_page.all_phone_from_home_page == merge_phones_like_on_homepage(contact_from_edit_page)


#def test_phones_on_viewpage(app):
#    contact_from_view_page = app.group.get_contact_from_view_page(0)
#    contact_from_edit_page = app.group.get_contact_from_edit_page(0)
#    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(address_data):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address_data.home_phone, address_data.mobile_phone, address_data.work_phone]))))

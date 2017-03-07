from model.group import Group
from timeit import timeit
from model.group_address import Address_data
from test.test_string_value import merge_emails
from test.test_string_value import merge_phones_like_on_homepage

#def test_group_list(app, db):
#    print(timeit(lambda: app.group.get_group_list(), number=1))
#    def clean(group):
#        return Group(id=group.id, name=group.name.strip())
#    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
#    assert False


def test_contact_list_db(app, db):

    def clean(address_data):
        return Address_data(id=address_data.id, firstname=address_data.firstname, lastname=address_data.lastname,
                            address=address_data.address.strip(),
                            all_phone_from_home_page=merge_phones_like_on_homepage(address_data),
                            all_emails=merge_emails(address_data))

    ui_contacts = app.group.get_contact_rows()
    db_contacts = map(clean, db.get_contact_list())
    #db_contacts = db.get_contact_list()
    assert sorted(ui_contacts, key=Group.id_or_max) == sorted(db_contacts, key=Group.id_or_max)

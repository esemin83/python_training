import string
import random

#def test_to_test(app):
#    old_contacts = app.group.get_contact_rows()
#    new_contacts = app.group.get_contact_rows()
#    old_contacts[0:1] = []
#    print(list(old_contacts), list(new_contacts))
#    new_contacts[0:1] = []
#    print(list(old_contacts), list(new_contacts))
#    assert len(old_contacts) == len(new_contacts)


#def test(app):
#    contact_from_edit_page = app.group.get_contact_from_edit_page(0)
#    print(contact_from_edit_page)


#def test_1(app):
#    contact_from_home_page = app.group.get_contact_rows()[0]
#    #contact_from_home_page.all_phone_from_home_page
#    print(contact_from_home_page)


#def test_2(app):
#    sss = app.group.get_contact_from_view_page(0)
#    print(sss)

def test(app):
    s = random_numbers(10)
    m = random_mail("@mail.ru", 10)
    print(s, "\n" + m)


def random_numbers(maxlen):
    numbers = string.digits + " "*3 + "(" + ")" + "-"
    return "".join([random.choice(numbers) for x in range(maxlen)])


def random_mail(domen, maxlen):
    value = string.ascii_letters + string.digits
    return "".join([random.choice(value) for x in range(random.randrange(maxlen))]) + domen


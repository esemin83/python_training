#from model.group_address import Address_data


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_contact()
    app.session.logout()
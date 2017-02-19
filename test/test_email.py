

def test_email_on_homepage(app):
    email_from_homepage = app.group.get_contact_rows()[0]
    email_from_edit_page = app.group.get_contact_from_edit_page(0)
    x = email_from_homepage.all_emails
    y = merge_emails(email_from_edit_page)
    print(x, y)
    assert email_from_homepage.all_emails == merge_emails(email_from_edit_page)


def merge_emails(address_data):
    return "\n".join([address_data.email_1, address_data.email_2])

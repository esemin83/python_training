

def test_address(app):
    address_from_homepage = app.group.get_contact_rows()[0]
    address_from_edit_page = app.group.get_contact_from_edit_page(0)
    assert address_from_homepage.address == address_from_edit_page.address


#def test_address_new(app):
#    address_from_homepage = app.group.get_contact_rows()[0]
#    address_from_edit_page = app.group.get_contact_from_edit_page(0)
#    assert address_from_homepage.address == address_from_edit_page.address


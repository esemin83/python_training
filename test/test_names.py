

def test_names_on_homepage(app):
    names_from_homepage = app.group.get_contact_rows()[0]
    names_from_edit_page = app.group.get_contact_from_edit_page(0)
    #x = merge_names(names_from_homepage)
    #y = merge_names(names_from_edit_page)
    #print(x, y)
    #assert x == y
    assert merge_names(names_from_homepage) == merge_names(names_from_edit_page)


def merge_names(address_data):
    return "\n".join([address_data.lastname, address_data.firstname])
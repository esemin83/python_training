#import pytest
#from fixture.application import Application
from model.group import Group


#@pytest.fixture
#def app(request):
#    fixture = Application()
#    request.addfinalizer(fixture.destroy)
#    return fixture


def test_del_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username= "admin", password="secret")
    app.group.modify_first_group(Group(name="test_modify", header="test_modify", footer="test_modify"))
    app.session.logout()

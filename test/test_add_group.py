# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username= "admin", password="secret")
    app.group.create(Group(name="test_5", header="test_5", footer="test_5"))
    app.session.logout()

def test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_1", header="test_1", footer="test_1"))


def test_add_group_new(app):
    app.group.create(Group(name="test", header="test"))

# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test_for_modification"))
    app.group.modify_first_group(Group(header="new header"))


def test_modify_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test_for_modification"))
    app.group.modify_first_group(Group(footer="new footer"))


# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group name", header="group header", footer="group footer")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group_new(app):
    old_groups = app.group.get_group_list()
    group = Group(name="new group", header="new header")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

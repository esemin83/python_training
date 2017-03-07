# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="for_modification"))
    old_groups = app.group.get_group_list()
    group = Group(name="test_for_modification???")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_some_group(group, index)
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_modify_group_db(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="for_modification", header="for_modification", footer="for_modification"))
    old_groups = db.get_group_list()
    modify_data = Group(name="mmm", header="mmm", footer="mmm")
    group = random.choice(old_groups)
    app.group.modify_some_group_by_id(modify_data, group.id)
    modify_data.id = group.id
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(modify_data)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    #assert new_groups == old_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

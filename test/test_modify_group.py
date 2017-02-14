# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="for_modification"))
    old_groups = app.group.get_group_list()
    group = Group(name="test_for_modification???")
    #group.id = old_groups[index].id
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_some_group(group, index)
    #new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    #print(sorted(new_groups, key=Group.id_or_max))
    #print(sorted(old_groups, key=Group.id_or_max))
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count_groups() == 0:
#        app.group.create(Group(name="test_for_modification"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="new footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


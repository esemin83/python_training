# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="for_modification"))
    old_groups = app.group.get_group_list()
    group = Group(name="test_for_modification???")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
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


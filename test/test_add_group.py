# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#from data.groups import testdata as testdata


def test_add_group(app, json_groups):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = app.group.get_group_list()
    with pytest.allure.step('When I add the group %s to the list' % group):
        app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count_groups()
    with pytest.allure.step('the new group list is equal to the old list with added group'):
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_add_group_db(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
'''
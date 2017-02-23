from model.group import Group
from random import randrange


def test_del_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test_for_del"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_del_all_group(app):
    all_group = app.group.count_groups()
    if all_group == 0:
        pass
    else:
        for x in range(all_group):
            app.group.delete_first_group()


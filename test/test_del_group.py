from model.group import Group


def test_del_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="test_for_del"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    #new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups

# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*7
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + \
           [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 15)]
    for header in ["", random_string("header", 15)]
    for footer in ["", random_string("footer", 15)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_add_group(app):
#    testdata = [
#        Group(name="group name", header="group header", footer="group footer"),
#        Group(name="new group", header="new header")
#    ]
#    for group in testdata:
#        pass
        #old_groups = app.group.get_group_list()
        ##group = Group(name="group name", header="group header", footer="group footer")
        #app.group.create(group)
        #assert len(old_groups) + 1 == app.group.count_groups()
        #new_groups = app.group.get_group_list()
        #old_groups.append(group)
        #assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

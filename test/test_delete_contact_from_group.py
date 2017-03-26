import random
from model.group import Group
from model.group_address import Address_data


def test_del_contact_from_group_contact__in_group_list(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name_1", header="header_1", footer="footer_1"))
    if len(orm.get_contact_list()) == 0:
        app.group.add_new_address_form(Address_data(firstname="Chuck", middlename="S", lastname="Norris", nickname="CN",
                                                    company="USA", address="Texas"))
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    if len(orm.get_contact_in_groups(group)) != 0:
        cnt_in_grp_old = orm.get_contact_in_groups(group)
        contact_to_del = random.choice(cnt_in_grp_old)
        app.group.delete_contact_from_group(contact_to_del.id, group.id)
        cnt_in_grp_new = orm.get_contact_in_groups(group)
        cnt_in_grp_old.remove(contact_to_del)
        assert sorted(cnt_in_grp_old, key=Address_data.id_or_max) == sorted(cnt_in_grp_new, key=Address_data.id_or_max)
        print('\n', 'old = ', cnt_in_grp_old)
        print('\n', 'new = ', cnt_in_grp_new)
    else:
        cnt_not_in_grp = orm.get_contact_not_in_groups(group)
        if len(cnt_not_in_grp) == 0:
            contact_to_add = Address_data(firstname="FIRSTNAME", middlename="D", lastname="LASTNAME", nickname="RR",
                                          company="USA", address="Texas")
            app.group.add_new_address_form(contact_to_add)
        cnt_to_add = random.choice(cnt_not_in_grp)
        app.group.add_contact_to_group_v01(cnt_to_add.id, group.id)
        cnt_in_grp_old = orm.get_contact_in_groups(group)
        contact_to_del = random.choice(cnt_in_grp_old)
        app.group.delete_contact_from_group(contact_to_del.id, group.id)
        cnt_in_grp_new = orm.get_contact_in_groups(group)
        cnt_in_grp_old.remove(contact_to_del)
        assert sorted(cnt_in_grp_old, key=Address_data.id_or_max) == sorted(cnt_in_grp_new, key=Address_data.id_or_max)
        print('\n', 'old = ', cnt_in_grp_old)
        print('\n', 'new = ', cnt_in_grp_new)




def test_del_all_group(app, db):
    all_group = db.get_group_list()
    if len(all_group) == 0:
        pass
    else:
        for x in range(len(all_group)):
            app.group.delete_first_group()

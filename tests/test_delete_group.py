# -*- coding: utf-8 -*-
from random import choice

from model.group import Group


def test_delete_groups(app, db, check_ui):
    app.group.group_must_exist(db.get_group_list())
    old_groups = db.get_group_list()
    group = choice(old_groups)

    app.group.delete_group_by_id(id=group.id)

    new_groups = app.group.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# -*- coding: utf-8 -*-
from random import choice

from common.data_generator import random_int
from model.group import Group


def test_update_group(app, db, check_ui):
    app.group.group_must_exist(db.get_group_list())
    old_groups = db.get_group_list()
    old_group = choice(old_groups)
    updated_group = Group(
        name=f"test update name{random_int()}",
        header=f"test update header{random_int()}",
        footer=f"test update footer{random_int()}",
        id=old_group.id
    )

    app.group.update_group_by_id(group=updated_group, id=old_group.id)

    new_groups = app.group.get_group_list()
    old_groups.remove(old_group)
    old_groups.append(updated_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_update_only_name_of_group(app, db, check_ui):
    app.group.group_must_exist(db.get_group_list())
    old_groups = db.get_group_list()
    old_group = choice(old_groups)
    updated_group = Group(name=f"test update name{random_int()}", id=old_group.id)

    app.group.update_group_by_id(group=updated_group, id=old_group.id)

    new_groups = db.get_group_list()
    old_groups.remove(old_group)
    old_groups.append(updated_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_groups(app):
    app.group.group_must_exist()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    del old_groups[0]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_groups(app):
    app.group.group_must_exist()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    del old_groups[0]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

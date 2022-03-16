# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_delete_groups(app):
    app.group.group_must_exist()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index=index)
    assert len(old_groups) - 1 == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    del old_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

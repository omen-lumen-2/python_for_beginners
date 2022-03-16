# -*- coding: utf-8 -*-
from random import randint, randrange

from model.group import Group


def test_update_group(app):
    app.group.group_must_exist()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(
        name="test update name",
        header="test update header",
        footer="test update footer",
        id=old_groups[index].id
    )
    app.group.update_group_by_index(group=group, index=index)
    assert len(old_groups) == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_update_only_name_of_group(app):
    app.group.group_must_exist()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name=f"test update name{randint(1,100)}", id=old_groups[index].id)
    app.group.update_group_by_index(group=group, index=index)
    assert len(old_groups) == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

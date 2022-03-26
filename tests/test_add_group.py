# -*- coding: utf-8 -*-

from model.group import Group


def test_add_new_group_from_python_file(app, data_groups):
    old_groups = app.group.get_group_list()
    group = data_groups
    app.group.create(group=group)
    assert len(old_groups) + 1 == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_new_group_from_json_file(app, json_groups):
    old_groups = app.group.get_group_list()
    group = json_groups
    app.group.create(group=group)
    assert len(old_groups) + 1 == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

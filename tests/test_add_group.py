# -*- coding: utf-8 -*-
from random import randint

import pytest

from common.data_generator import random_string
from model.group import Group

groups = [
    Group(name=name, header=header, footer=footer)
    for name in [None, random_string(prefix='name')]
    for header in [None, random_string(prefix='header')]
    for footer in [None, random_string(prefix='footer')]
    ]


@pytest.mark.parametrize('groups', groups, ids=[repr(x) for x in groups])
def test_add_new_group(app, groups):
    old_groups = app.group.get_group_list()
    group = groups
    app.group.create(group=group)
    assert len(old_groups) + 1 == app.group.get_count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

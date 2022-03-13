# -*- coding: utf-8 -*-
from random import randint

from model.group import Group


def test_update_group(app):
    app.group.group_must_exist()
    app.group.update_first_group(group=Group(
        name="test update name",
        header="test update header",
        footer="test update footer")
    )


def test_update_only_name_of_group(app):
    app.group.group_must_exist()
    app.group.update_first_group(group=Group(name=f"test update name{randint(1,100)}"))

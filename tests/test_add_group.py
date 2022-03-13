# -*- coding: utf-8 -*-
from random import randint

from model.group import Group


def test_add_new_group(app):
    app.group.create(group=Group(name="test name", header="test header", footer="test footer"))


def test_add_empty_group(app):
    app.group.create(group=Group())


def test_add_group_if_pass_only_name(app):
    app.group.create(group=Group(name=f"Name{randint(1,100)}"))

# -*- coding: utf-8 -*-
from random import randint

from model.group import Group


def test_add_new_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(group=Group(name="test name", header="test header", footer="test footer"))
    app.navigation.go_to_group_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(group=Group())
    app.navigation.go_to_group_page()
    app.session.logout()


def test_add_group_if_pass_only_name(app):
    app.session.login(login="admin", password="secret")
    app.group.create(group=Group(name=f"Name{randint(1,100)}"))
    app.navigation.go_to_group_page()
    app.session.logout()

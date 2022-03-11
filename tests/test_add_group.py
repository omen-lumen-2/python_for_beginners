# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(group=Group(name="test name", header="test header", footer="test footer"))
    app.navigation.go_to_group_page()
    app.session.logout()

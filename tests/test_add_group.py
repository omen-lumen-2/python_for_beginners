# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_groups(app):
    app.login(login="admin", password="secret")
    app.create_group(group=Group(name="test name", header="test header", footer="test footer"))
    app.open_groups_page()
    app.logout()
# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group(app):
    app.session.login(login="admin", password="secret")
    app.group.update_first_group(group=Group(
        name="test update name",
        header="test update header",
        footer="test update footer")
    )
    app.navigation.go_to_group_page()
    app.session.logout()

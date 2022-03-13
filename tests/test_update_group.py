# -*- coding: utf-8 -*-
from random import randint

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

def test_update_only_name_of_group(app):
    app.session.login(login="admin", password="secret")
    app.group.update_first_group(group=Group(name=f"test update name{randint(1,100)}"))
    app.navigation.go_to_group_page()
    app.session.logout()

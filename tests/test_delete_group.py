# -*- coding: utf-8 -*-

def test_add_new_groups(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_first_group()
    app.navigation.go_to_group_page()
    app.session.logout()
# -*- coding: utf-8 -*-

def test_add_new_groups(app):
    app.group.group_must_exist()
    app.group.delete_first_group()

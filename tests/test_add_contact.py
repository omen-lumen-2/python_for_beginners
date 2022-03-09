# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_add_new_contact(app):
    app.login(login="admin", password="secret")
    app.create_new_contact(Contact(
        firstname="Test_first_name",
        middlename="Test_middle_name",
        email="test@test.test"
    ))
    app.go_to_home_page()
    app.logout()


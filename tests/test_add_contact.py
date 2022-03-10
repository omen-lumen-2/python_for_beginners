# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_add_new_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(
        firstname="Test_first_name",
        middlename="Test_middle_name",
        email="test@test.test"
    ))
    app.navigation.go_to_home_page()
    app.session.logout()


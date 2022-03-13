# -*- coding: utf-8 -*-
from random import randint

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


def test_add_empty_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact())
    app.navigation.go_to_home_page()
    app.session.logout()


def test_add_contact_if_pass_only_firstname(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(firstname=f"Test_first_name{randint(1,100)}"))
    app.navigation.go_to_home_page()
    app.session.logout()

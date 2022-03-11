# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_update_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.update_first_contact(Contact(
        firstname="Test_first_name",
        middlename="Test_middle_name",
        email="test@test.test"
    ))
    app.session.logout()

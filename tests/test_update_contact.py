# -*- coding: utf-8 -*-
from random import randint

from model.сontact import Contact


def test_update_contact(app):
    app.contact.update_first_contact(Contact(
        firstname="Test_first_name",
        middlename="Test_middle_name",
        email="test@test.test"
    ))


def test_update_only_firstname_of_contact(app):
    app.contact.update_first_contact(Contact(firstname=f"Update_first_name{randint(1,100)}"))

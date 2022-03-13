# -*- coding: utf-8 -*-

def test_delete_contact(app):
    app.contact.contact_must_exist()
    app.contact.delete_first_contact()

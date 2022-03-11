# -*- coding: utf-8 -*-

def test_delete_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_first_contact()
    app.navigation.go_to_home_page()
    app.session.logout()

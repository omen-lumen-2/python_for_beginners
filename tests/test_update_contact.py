# -*- coding: utf-8 -*-
from random import randint

from model.сontact import Contact


def test_update_contact(app):
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test_first_name",
                      lastname="Test_lastname",
                      email="test@test.test",
                      id=old_contacts[0].id)
    app.contact.update_first_contact(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_only_firstname_of_contact(app):
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"Update_first_name{randint(1,100)}",
                      lastname=old_contacts[0].lastname,
                      id=old_contacts[0].id)
    app.contact.update_first_contact(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# -*- coding: utf-8 -*-
from random import randint

from model.сontact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"Test_first_name{randint(1,100)}", lastname=f"Test_lastname{randint(1,100)}",\
                      email="test@test.test")
    app.contact.create(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact()
    app.contact.create(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    contact.firstname = ''
    contact.lastname = ''
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_if_pass_only_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"Test_first_name{randint(1,100)}")
    app.contact.create(contact=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    contact.lastname = ''
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

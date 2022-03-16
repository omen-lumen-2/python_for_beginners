# -*- coding: utf-8 -*-
from random import randint, randrange

from model.сontact import Contact


def test_update_contact(app):
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname=f"Test_first_name{randint(1,100)}",
                      lastname=f"Test_lastname{randint(1,100)}",
                      email="test@test.test",
                      id=old_contacts[index].id)
    app.contact.update_contact_by_index(contact=contact, index=index)
    assert len(old_contacts) == app.contact.get_count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_only_firstname_of_contact(app):
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname=f"Update_first_name{randint(1,100)}",
                      lastname=old_contacts[0].lastname,
                      id=old_contacts[index].id)
    app.contact.update_contact_by_index(contact=contact, index=index)
    assert len(old_contacts) == app.contact.get_count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

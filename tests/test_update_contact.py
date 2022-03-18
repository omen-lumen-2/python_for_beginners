# -*- coding: utf-8 -*-
from random import randrange

from common.data_generator import random_int, random_email
from model.сontact import Contact


def test_update_contact(app):
    # Given
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    index = 0
    contact = Contact(firstname=f"Test_first_name{random_int()}",
                      lastname=f"Test_lastname{random_int()}",
                      email=random_email(),
                      email2=random_email(),
                      email3=random_email())

    # When
    app.contact.update_contact_by_index(contact=contact, index=index)
    # Then
    contact.id = old_contacts[index].id
    contact.address = old_contacts[index].address
    assert len(old_contacts) == app.contact.get_count_contact()
    old_contacts[index] = contact
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_only_firstname_of_contact(app):
    # Given
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname=f"Update_first_name{random_int()}")
    # When
    app.contact.update_contact_by_index(contact=contact, index=index)
    # Then
    contact.lastname = old_contacts[index].lastname
    contact.id = old_contacts[index].id
    contact.address = old_contacts[index].address
    assert len(old_contacts) == app.contact.get_count_contact()
    old_contacts[index] = contact
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

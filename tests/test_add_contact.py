# -*- coding: utf-8 -*-

from common.data_generator import random_email, random_int
from model.сontact import Contact


def test_add_new_contact(app):
    # Given
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"Test_first_name{random_int()}", lastname=f"Test_lastname{random_int()}",\
                      email=random_email())
    # When
    app.contact.create(contact=contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    # Given
    old_contacts = app.contact.get_contact_list()
    contact = Contact()
    # When
    app.contact.create(contact=contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    contact.firstname = ''
    contact.lastname = ''
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_if_pass_only_firstname(app):
    # Given
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=f"Test_first_name{random_int()}")
    # When
    app.contact.create(contact=contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    contact.lastname = ''
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

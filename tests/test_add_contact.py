# -*- coding: utf-8 -*-

from model.сontact import Contact


def test_add_new_contact_from_python_file(app, data_contacts):
    old_contacts = app.contact.get_contact_list()
    expect_contact = data_contacts
    # When
    app.contact.create(contact=expect_contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    old_contacts.append(expect_contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_contact_from_json_file(app, json_contacts):
    old_contacts = app.contact.get_contact_list()
    expect_contact = json_contacts
    # When
    app.contact.create(contact=expect_contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    old_contacts.append(expect_contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# -*- coding: utf-8 -*-

from model.сontact import Contact


def test_add_new_contact_from_python_file(app, db, check_ui, data_contacts):
    expect_contact = data_contacts
    old_contacts = db.get_contact_list()

    app.contact.create(contact=expect_contact)

    old_contacts.append(expect_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_add_new_contact_from_json_file(app, db, check_ui, json_contacts):
    expect_contact = json_contacts
    old_contacts = db.get_contact_list()

    app.contact.create(contact=expect_contact)

    old_contacts.append(expect_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

# -*- coding: utf-8 -*-
from random import choice

from common.data_generator import random_email, random_string
from model.сontact import Contact


def test_update_contact(app, db, check_ui):
    app.contact.contact_must_exist(len(db.get_contact_list()))
    old_contacts = db.get_contact_list()
    old_contact = choice(old_contacts)
    contact = Contact(firstname=random_string(prefix='firstname', maxlen=5),
                      lastname=random_string(prefix='lastname', maxlen=5),
                      email=random_email(),
                      email2=random_email(),
                      email3=random_email(),
                      id=old_contact.id)

    app.contact.update_contact_by_id(contact=contact, id=contact.id)

    contact.address = old_contact.address
    old_contacts.remove(old_contact)
    old_contacts.append(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_update_only_firstname_of_contact(app, db, check_ui):
    app.contact.contact_must_exist(len(db.get_contact_list()))
    old_contacts = db.get_contact_list()
    old_contact = choice(old_contacts)
    contact = Contact(id = old_contact.id, firstname=random_string(prefix='firstname', maxlen=5))

    app.contact.update_contact_by_id(contact=contact, id=old_contact.id)

    contact.lastname = old_contact.lastname
    contact.address = old_contact.address
    old_contacts.remove(old_contact)
    old_contacts.append(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

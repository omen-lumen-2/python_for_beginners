# -*- coding: utf-8 -*-
from random import choice

from model.сontact import Contact


def test_delete_contact(app, db, check_ui):
    app.contact.contact_must_exist(db.get_contact_list())
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)

    app.contact.delete_contact_by_id(id=contact.id)

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

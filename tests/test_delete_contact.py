# -*- coding: utf-8 -*-
from random import choice

from model.сontact import Contact


def test_delete_contact(app, db, check_ui):
    app.contact.contact_must_exist(len(db.get_contact_list()))
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)

    app.contact.delete_contact_by_id(id=contact.id)

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_delete_contact_with_group(app, db):
    # проверяем наличие хотя бы одной группы
    app.group.group_must_exist(len(db.get_group_list()))
    # создаем контакт с группой
    app.contact.create(contact=Contact(group_id=choice(db.get_group_list()).id))
    contact_id = db.get_last_create_contact_id()

    app.contact.delete_contact_by_id(id=contact_id)

    assert contact_id not in db.get_contacts_id_with_group()

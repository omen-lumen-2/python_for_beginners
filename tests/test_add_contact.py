# -*- coding: utf-8 -*-
from random import choice

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


def test_add_new_contact_with_select_group(app, db):
    # проверяем наличие хотя бы одной группы
    app.group.group_must_exist(len(db.get_group_list()))
    group = choice(db.get_group_list())

    app.contact.create(contact=Contact(group_id=group.id))

    # проверить что в бд пользователь добавлен в группу
    last_contact_id = db.get_last_create_contact_id()
    assert db.get_group_of_contact(contact_id=last_contact_id) == group.id


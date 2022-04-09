# -*- coding: utf-8 -*-
import time
from random import choice

from common.data_generator import random_email, random_string
from model.group import Group
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


def test_add_contact_to_group(app, db):
    # проверяем наличие хотя бы одной группы
    app.group.group_must_exist(len(db.get_group_list()))
    group = choice(db.get_group_list())

    # проверяем наличие контактов без групп
    if len(db.get_contact_id_list_by_link_group(link_to_group=False)) == 0:
        app.contact.create(contact=Contact())
    contact_id = choice(db.get_contact_id_list_by_link_group(link_to_group=False))
    app.contact.add_contact_to_group(contact_id=contact_id, group_id=group.id)

    # проверить что в бд пользователь добавлен в группу
    assert db.get_group_of_contact(contact_id=contact_id) == group.id


def test_change_group_in_contact(app, db):
    # проверяем наличие хотя бы двух групп
    while len(db.get_group_list()) < 2:
        app.group.create(Group(name=random_string('Name'),
                               header=random_string('Header'),
                               footer=random_string('footer')))
    exist_group = db.get_group_list()
    # создаем контакт с группой
    raw_group_id = choice(exist_group).id
    app.contact.create(contact=Contact(firstname=random_string('Firstname', 7), group_id=raw_group_id))
    # добавляем контакт в группу отличной от изначальной
    contact_id = db.get_last_create_contact_id()
    new_group = choice([group.id for group in exist_group if group.id != raw_group_id])
    app.contact.add_contact_to_group(contact_id=contact_id, group_id=new_group)
    # проверить что в бд пользователь добавлен в группу
    assert db.get_group_of_contact(contact_id=contact_id) == new_group

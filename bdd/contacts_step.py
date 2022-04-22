from random import choice

from pytest_bdd import given, when, then, parsers

from common.data_generator import random_string, random_email
from model.сontact import Contact


@given('a raw contact list', target_fixture="get_raw_list_contact")
def get_raw_list_contact(db):
    return db.get_contact_list()


@given(parsers.parse("a contact with {firstname}, {middlename}"), target_fixture="init_contact")
def init_contact(firstname, middlename):
    return Contact(firstname=firstname, middlename=middlename)


@when('i create new contact')
def add_new_contact(app, init_contact):
    app.contact.create(contact=init_contact)


@then('the new contact list is equal to raw contact list with created contact')
def verify_contact_added(db, get_raw_list_contact, init_contact):
    old_contacts = get_raw_list_contact
    old_contacts.append(init_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given("there must be at least one contact")
def validate_exist_at_least_one_contact(app, db):
    app.group.group_must_exist(len(db.get_group_list()))


@given("choice random contact", target_fixture="choice_random_contact")
def choice_random_contact(get_raw_list_contact):
    return choice(get_raw_list_contact)


@when("i delete selected contact")
def delete_contact(app, choice_random_contact):
    app.contact.delete_contact_by_id(id=choice_random_contact.id)


@then('the new contact list is equal to raw contact list without deleted contact')
def verify_contact_delete(db, get_raw_list_contact, choice_random_contact):
    new_contacts = db.get_contact_list()
    old_contacts = get_raw_list_contact
    old_contacts.remove(choice_random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given("a new data for contact", target_fixture="prepare_update_contact")
def prepare_update_contact(choice_random_contact):
    return Contact(firstname=random_string(prefix='firstname', maxlen=5),
                   lastname=random_string(prefix='lastname', maxlen=5),
                   email=random_email(),
                   email2=random_email(),
                   email3=random_email(),
                   id=choice_random_contact.id)


@when("i update selected contact")
def update_contact(app, prepare_update_contact):
    app.contact.update_contact_by_id(contact=prepare_update_contact, id=prepare_update_contact.id)


@then("the new contact list is equal to raw contact list without update contact")
def verify_contact_update(db, choice_random_contact, get_raw_list_contact, prepare_update_contact):
    updated_contact = prepare_update_contact
    updated_contact.address = choice_random_contact.address
    old_contacts = get_raw_list_contact
    old_contacts.remove(choice_random_contact)
    old_contacts.append(updated_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

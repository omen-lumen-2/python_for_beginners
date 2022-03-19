# -*- coding: utf-8 -*-
import pytest

from common.data_generator import random_email, random_string, random_phone_number
from model.сontact import Contact

contacts = [Contact(firstname=firstname, middlename=middlename, lastname=lastname, address=address,
                 homephone=homephone, email=email)
            for firstname in [None, random_string(prefix='firstname')]
            for middlename in [None, random_string(prefix='middlename')]
            for lastname in [None, random_string(prefix='lastname')]
            for address in [None, random_string(prefix='address')]
            for homephone in [None, random_phone_number()]
            for email in [None, random_email()]
            ]


@pytest.mark.parametrize('contact', contacts, ids=[repr(x) for x in contacts])
def test_add_new_contact(app, contact):
    # Given
    old_contacts = app.contact.get_contact_list()
    expect_contact = contact
    # When
    app.contact.create(contact=expect_contact)
    # Then
    assert len(old_contacts) + 1 == app.contact.get_count_contact()
    old_contacts.append(expect_contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

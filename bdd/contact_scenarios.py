from pytest_bdd import scenario
from .contacts_step import *


@scenario("contacts.feature", "Add new contact")
def test_add_contact():
    pass


@scenario("contacts.feature", "Delete contact")
def test_delete_contact():
    pass


@scenario("contacts.feature", "Update contact")
def test_update_contact():
    pass

from selenium import webdriver

from fixture.contact import Contact
from fixture.group import Group
from fixture.navigation import Navigation
from fixture.session import Session


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = Session(self)
        self.group = Group(self)
        self.navigation = Navigation(self)
        self.contact = Contact(self)

    def wd_quit(self):
        self.wd.quit()

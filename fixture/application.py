from selenium import webdriver

from fixture.common_action import CommonAction
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import Navigation
from fixture.session import Session


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.navigation = Navigation(self)
        self.contact = ContactHelper(self)
        self.action = CommonAction(self)

    def wd_quit(self):
        self.wd.quit()

    def is_not_valid(self):
        try:
            self.wd.current_url
            return False
        except:
            return True




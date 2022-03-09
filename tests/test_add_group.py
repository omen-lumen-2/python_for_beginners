# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from model.group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def test_add_new_groups(self):
        self.login(login="admin", password="secret")
        self.create_group( Group(name="test name", header="test header", footer="test footer"))
        self.open_groups_page()
        self.logout()

    def logout(self):
        wb = self.wb
        wb.find_element_by_link_text("Logout").click()

    def create_group(self, group):
        wb = self.wb
        # open groups page
        wb.find_element_by_link_text("groups").click()
        # move to create new group
        wb.find_element_by_name("new").click()
        # set values of new group
        wb.find_element_by_name("group_name").click()
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys(group.name)
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys(group.header)
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys(group.footer)
        # approve creation new group
        wb.find_element_by_name("submit").click()

    def open_groups_page(self):
        wb = self.wb
        wb.find_element_by_link_text("groups").click()

    def login(self, login, password):
        wb = self.wb
        # open authorize page
        wb.get("http://localhost/addressbook/group.php?delete=Delete+group%28s%29&selected%5B%5D=1")
        # input login
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(login)
        # input password
        wb.find_element_by_id("LoginForm").click()
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        # submit
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wb.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wb.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wb.quit()


if __name__ == "__main__":
    unittest.main()
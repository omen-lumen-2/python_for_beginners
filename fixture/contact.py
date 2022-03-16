from random import randint

from model.сontact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_group_form(self, contact):
        self.app.action.type_in_input_field_with_name(name="firstname", input_value=contact.firstname)
        self.app.action.type_in_input_field_with_name(name="lastname", input_value=contact.lastname)
        self.app.action.type_in_input_field_with_name(name="middlename", input_value=contact.middlename)
        self.app.action.type_in_input_field_with_name(name="email", input_value=contact.email)

    def create(self, contact):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # move to create new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact group
        self.fill_contact_group_form(contact)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # go to home page
        self.app.navigation.go_to_home_page()
        # invalidate contact cash
        self.contact_cash = None

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select edit element of table by index
        wd.find_elements_by_xpath("//img[@title='Edit']/..")[index].click()
        # fill contact group
        self.fill_contact_group_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@name='update']").click()
        # click in dialog to return home page
        wd.find_element_by_xpath("//div[@class='msgbox']//a").click()
        # invalidate contact cash
        self.contact_cash = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select contact in list of exist contacts by index
        wd.find_elements_by_xpath("//input[@name='selected[]']")[index].click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deleting on dialog
        wd.switch_to.alert.accept()
        # wait update screen
        wd.find_element_by_xpath("//input[@name='searchstring']").click()
        # go to home page
        self.app.navigation.go_to_home_page()
        # invalidate contact cash
        self.contact_cash = None

    def contact_must_exist(self):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # create contact if contact not exist
        if self.get_count_contact() == 0:
            self.create(contact=Contact(firstname=f"Test_name{randint(1,100)}",
                                  middlename=f"Test_middlename{randint(1,100)}",
                                  email=f"{randint(1,100)}@test.test"))

    def get_count_contact(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            # go to home page
            self.app.navigation.go_to_home_page()
            self.contact_cash = []
            for elements in wd.find_elements_by_xpath("//tr[@name='entry']"):
                firstname = elements.find_element_by_xpath(".//td[3]").text
                lastname = elements.find_element_by_xpath(".//td[2]").text
                id = elements.find_element_by_name("selected[]").get_attribute('value')
                self.contact_cash.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return self.contact_cash.copy()

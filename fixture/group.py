from random import randint

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        self.app.action.type_in_input_field_with_name(name="group_name", input_value=group.name)
        self.app.action.type_in_input_field_with_name(name="group_header", input_value=group.header)
        self.app.action.type_in_input_field_with_name(name="group_footer", input_value=group.footer)


    def create(self, group):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # move to create new group
        wd.find_element_by_name("new").click()
        # set values of new group
        self.fill_group_form(group)
        # approve creation new group
        wd.find_element_by_name("submit").click()
        # open groups page
        self.app.navigation.go_to_group_page()
        # invalidate group cash
        self.group_cash = None

    def update_first_group(self, group):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select first group in list of exist group
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select Edit GROUP
        wd.find_element_by_xpath("//input[@name='edit']").click()
        # set new values
        self.fill_group_form(group)
        # approve creation new group
        wd.find_element_by_name("update").click()
        # open groups page
        self.app.navigation.go_to_group_page()
        # invalidate group cash
        self.group_cash = None

    def delete_first_group(self):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select first group in list of exist group
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select DELETE GROUP(s)
        wd.find_element_by_xpath("//input[@name='delete']").click()
        # open groups page
        self.app.navigation.go_to_group_page()
        # invalidate group cash
        self.group_cash = None

    def group_must_exist(self):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # create group if group not exist
        if self.get_count_group() == 0:
            self.create(group=Group(name=f"Test_name{randint(1,100)}",
                                    header=f"Test_header{randint(1,100)}",
                                    footer=f"Test_footer{randint(1,100)}"))

    def get_count_group(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            # open groups page
            self.app.navigation.go_to_group_page()
            self.group_cash = []
            for elements in wd.find_elements_by_xpath("//span[@class='group']"):
                text = elements.text
                id = elements.find_element_by_name("selected[]").get_attribute('value')
                self.group_cash.append(Group(name=text, id=id))
        return self.group_cash.copy()

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        self.app.action.type_in_input_field_with_name(name="group_name", input_value=group.name)
        self.app.action.type_in_input_field_with_name(name="group_name", input_value=group.header)
        self.app.action.type_in_input_field_with_name(name="group_name", input_value=group.footer)


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

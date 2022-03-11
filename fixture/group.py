class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # move to create new group
        wd.find_element_by_name("new").click()
        # set values of new group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # approve creation new group
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select first group in list of exist group
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select DELETE GROUP(s)
        wd.find_element_by_xpath("//input[@name='delete']").click()

    def update_first_group(self, group):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select first group in list of exist group
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select Edit GROUP
        wd.find_element_by_xpath("//input[@name='edit']").click()
        # set new values
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # approve creation new group
        wd.find_element_by_name("update").click()

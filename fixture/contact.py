class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_group_form(self, contact):
        self.app.action.type_in_input_field_with_name(name="firstname", input_value=contact.firstname)
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

    def update_first_contact(self, contact):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select edit in first element of table
        wd.find_element_by_xpath("//img[@title='Edit']/..").click()
        # fill contact group
        self.fill_contact_group_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@name='update']").click()
        # click in dialog to return home page
        wd.find_element_by_xpath("//div[@class='msgbox']//a").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select first contact in list of exist contacts
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deleting on dialog
        wd.switch_to.alert.accept()
        # wait update screen
        wd.find_element_by_xpath("//input[@name='searchstring']").click()


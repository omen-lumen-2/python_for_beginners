class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # move to create new contact
        wd.find_element_by_link_text("add new").click()
        # input firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # input middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # input email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # select edit in first element of table
        wd.find_element_by_xpath("//img[@title='Edit']/..").click()
        # input firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # input middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # input email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit
        wd.find_element_by_xpath("//input[@name='update']").click()
        # click in dialog to return home page
        wd.find_element_by_xpath("//div[@class='msgbox']//a").click()


    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact in list of exist contacts
        wd.find_element_by_xpath("//input[@name='selected[]']").click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deleting on dialog
        wd.switch_to.alert.accept()
        # wait update screen
        wd.find_element_by_xpath("//input[@name='searchstring']").click()


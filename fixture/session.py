
class Session:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        # open authorize page
        wd.get("http://localhost/addressbook/group.php?delete=Delete+group%28s%29&selected%5B%5D=1")
        # input login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_id("LoginForm").click()
        # input password
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # submit
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
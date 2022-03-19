
class Session:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        # open authorize page
        wd.get(self.app.base_url)
        # input login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        # input password
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # submit
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_as(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == f"({user_name})"

    def ensure_login(self, login, password):
        if self.is_logged_in():
            if self.is_logged_as(user_name=login):
                return
            else:
                self.logout()
        self.login(login=login, password=password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()



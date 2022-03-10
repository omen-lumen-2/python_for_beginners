class Navigation:
    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
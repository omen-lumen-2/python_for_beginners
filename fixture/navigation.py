import allure


class Navigation:
    def __init__(self, app):
        self.app = app

    @allure.step("Переход на страницу групп")
    def go_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    @allure.step("Переход на домашнию страницу")
    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_elements_by_xpath("//input[@name='searchstring']")) > 0):
            wd.find_element_by_link_text("home").click()

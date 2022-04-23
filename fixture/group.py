from random import randint

import allure

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    @allure.step("Заполнение формы группы")
    def fill_group_form(self, group):
        self.app.action.type_in_input_field_with_name(name="group_name", input_value=group.name)
        self.app.action.type_in_input_field_with_name(name="group_header", input_value=group.header)
        self.app.action.type_in_input_field_with_name(name="group_footer", input_value=group.footer)

    @allure.step("Создание группы")
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

    @allure.step("Обновление группы по индексу")
    def update_group_by_index(self, group, index):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select group in list of exist group by index
        self.select_group_by_index(index)
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

    @allure.step("Обновление группы по идентификатору")
    def update_group_by_id(self, group, id):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select group in list of exist group by id
        self.select_group_by_id(id=id)
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

    @allure.step("Удаление группы по индексу")
    def delete_group_by_index(self, index):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select group in list of exist group by index
        self.select_group_by_index(index)
        # select DELETE GROUP(s)
        wd.find_element_by_xpath("//input[@name='delete']").click()
        # open groups page
        self.app.navigation.go_to_group_page()
        # invalidate group cash
        self.group_cash = None

    @allure.step("Выделение группу по индексу")
    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(f"//input[@name='selected[]']")[index].click()

    @allure.step("Удаление группы по индентификатору")
    def delete_group_by_id(self, id):
        wd = self.app.wd
        # open groups page
        self.app.navigation.go_to_group_page()
        # select group in list of exist group by id
        self.select_group_by_id(id=id)
        # select DELETE GROUP(s)
        wd.find_element_by_xpath("//input[@name='delete']").click()
        # open groups page
        self.app.navigation.go_to_group_page()
        # invalidate group cash
        self.group_cash = None

    @allure.step("Выделение группу по индентификатору")
    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(f"//input[@value='{id}']").click()

    @allure.step("Проверка наличие хотя бы одной группы")
    def group_must_exist(self, count_group):
        # open groups page
        self.app.navigation.go_to_group_page()
        # create group if group not exist
        if count_group == 0:
            self.create(group=Group(name=f"Test_name{randint(1,100)}",
                                    header=f"Test_header{randint(1,100)}",
                                    footer=f"Test_footer{randint(1,100)}"))

    @allure.step("Получение количества групп")
    def get_count_group(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    group_cash = None

    @allure.step("Получение списка групп")
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

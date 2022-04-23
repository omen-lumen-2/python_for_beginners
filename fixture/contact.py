from random import randint

import allure

from model.сontact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    @allure.step("Заполнение формы создания контакта")
    def fill_contact_group_form(self, contact):
        self.app.action.type_in_input_field_with_name(name="firstname", input_value=contact.firstname)
        self.app.action.type_in_input_field_with_name(name="lastname", input_value=contact.lastname)
        self.app.action.type_in_input_field_with_name(name="middlename", input_value=contact.middlename)
        self.app.action.type_in_input_field_with_name(name="address", input_value=contact.address)
        # phone
        self.app.action.type_in_input_field_with_name(name="home", input_value=contact.homephone)
        self.app.action.type_in_input_field_with_name(name="work", input_value=contact.workphone)
        self.app.action.type_in_input_field_with_name(name="mobile", input_value=contact.mobilephone)
        self.app.action.type_in_input_field_with_name(name="phone2", input_value=contact.secondaryphone)
        # email
        self.app.action.type_in_input_field_with_name(name="email", input_value=contact.email)
        self.app.action.type_in_input_field_with_name(name="email2", input_value=contact.email2)
        self.app.action.type_in_input_field_with_name(name="email3", input_value=contact.email3)
        # group
        self.app.action.select_option_on_value(name_select='new_group', group_id=contact.group_id)

    @allure.step("Создание нового контакта")
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
        # go to home page
        self.app.navigation.go_to_home_page()
        # invalidate contact cash
        self.contact_cash = None

    @allure.step("Обновление контакта по индексу")
    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select edit element of table by index
        self.open_contact_for_edit_by_index(index)
        # fill contact group
        self.fill_contact_group_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@name='update']").click()
        # click in dialog to return home page
        wd.find_element_by_xpath("//div[@class='msgbox']//a").click()
        # invalidate contact cash
        self.contact_cash = None

    @allure.step("Обновление контакта по идентификатору")
    def update_contact_by_id(self, contact, id):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select edit element of table by id
        self.open_contact_for_edit_by_id(id)
        # fill contact group
        self.fill_contact_group_form(contact)
        # submit
        wd.find_element_by_xpath("//input[@name='update']").click()
        # click in dialog to return home page
        wd.find_element_by_xpath("//div[@class='msgbox']//a").click()
        # invalidate contact cash
        self.contact_cash = None

    @allure.step("Добавление контакта в группу")
    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select contact in list of exist contacts by id
        wd.find_element_by_xpath(f"//input[@value='{contact_id}']").click()
        # group
        self.app.action.select_option_on_value(name_select='to_group', group_id=group_id)
        # submit add
        wd.find_element_by_xpath("//input[@name='add']").click()
        # go to home page
        self.app.navigation.go_to_home_page()

    @allure.step("Удаление контакта по индексу")
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select contact in list of exist contacts by index
        wd.find_elements_by_xpath("//input[@name='selected[]']")[index].click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deleting on dialog
        wd.switch_to.alert.accept()
        # wait update screen
        wd.find_element_by_xpath("//input[@name='searchstring']").click()
        # go to home page
        self.app.navigation.go_to_home_page()
        # invalidate contact cash
        self.contact_cash = None

    @allure.step("Удаление контакта по идентификатору")
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # select contact in list of exist contacts by id
        wd.find_element_by_xpath(f"//input[@value='{id}']").click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deleting on dialog
        wd.switch_to.alert.accept()
        # wait update screen
        wd.find_element_by_xpath("//input[@name='searchstring']").click()
        # go to home page
        self.app.navigation.go_to_home_page()
        # invalidate contact cash
        self.contact_cash = None

    @allure.step("Проверка существования контакта")
    def contact_must_exist(self, count_contact):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        # create contact if contact not exist
        if count_contact == 0:
            self.create(contact=Contact(firstname=f"Test_name{randint(1,100)}",
                                  middlename=f"Test_middlename{randint(1,100)}",
                                  email=f"{randint(1,100)}@test.test"))

    @allure.step("Получение количества контактов")
    def get_count_contact(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cash = None

    @allure.step("Получение списка доступных фильмов")
    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            # go to home page
            self.app.navigation.go_to_home_page()
            self.contact_cash = []
            for elements in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = elements.find_element_by_name("selected[]").get_attribute('value')
                lastname = elements.find_element_by_xpath(".//td[2]").text
                firstname = elements.find_element_by_xpath(".//td[3]").text
                address = elements.find_element_by_xpath(".//td[4]").text
                all_email_address = elements.find_element_by_xpath(".//td[5]").text
                all_phones = elements.find_element_by_xpath(".//td[6]").text
                self.contact_cash.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                            all_email_address=all_email_address, all_phones=all_phones))
        return self.contact_cash.copy()

    @allure.step("Получение информации контакта с домашней страницы")
    def get_contact_info_from_home_page(self, index):
        wd = self.app.wd
        # go to home page
        self.app.navigation.go_to_home_page()
        row_table = wd.find_element_by_xpath(f"//tr[@name='entry'][{index+1}]")
        id = row_table.find_element_by_name("selected[]").get_attribute('value')
        lastname = row_table.find_element_by_xpath(".//td[2]").text
        firstname = row_table.find_element_by_xpath(".//td[3]").text
        address = row_table.find_element_by_xpath(".//td[4]").text
        all_email_address = row_table.find_element_by_xpath(".//td[5]").text
        all_phones = row_table.find_element_by_xpath(".//td[6]").text
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       all_email_address=all_email_address, all_phones=all_phones)

    @allure.step("Переход на страницу редактирования контактка по индексу")
    def open_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']/..")[index].click()

    @allure.step("Переход на страницу редактирования контакта по идетификатору")
    def open_contact_for_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(f"//a[contains(@href,'edit.php?id={id}')]").click()

    @allure.step("Получение информации контакта со страницы редактирования")
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        address = wd.find_element_by_name("address").text
        # phone
        homephone = wd.find_element_by_name("home").get_attribute('value')
        workphone = wd.find_element_by_name("work").get_attribute('value')
        mobilephone = wd.find_element_by_name("mobile").get_attribute('value')
        secondaryphone = wd.find_element_by_name("phone2").get_attribute('value')
        # email
        email = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)


class CommonAction:
    def __init__(self, app):
        self.app = app

    def type_in_input_field_with_name(self, name, input_value):
        wd = self.app.wd
        if input_value is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(input_value)

    def select_option_on_value(self, name_select, group_id):
        wd = self.app.wd
        if group_id is not None:
            wd.find_element_by_xpath(f"//select[@name='{name_select}']/option[@value='{group_id}']").click()

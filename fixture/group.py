

class GroupHelper:
#####################################################################################################
    # groups metods

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.init_group_creation()
        # fill group form
        self.fill_group_form(group)
        # submit creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def init_group_creation(self):
        # init group creation
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        # return to group page
        self.return_to_group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_element_by_name("selected[]").text)

#####################################################################################################
    # contact metods

    def add_new_address_form(self, address_data):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_address_form(address_data)
        # submit contact creation
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_address_form(self, address_data):
        self.change_field_value("firstname", address_data.firstname)
        self.change_field_value("middlename", address_data.middlename)
        self.change_field_value("lastname", address_data.lastname)
        self.change_field_value("nickname", address_data.nickname)
        self.change_field_value("company", address_data.company)
        self.change_field_value("address", address_data.address)
        self.change_field_value("home", address_data.home_phone)
        self.change_field_value("mobile", address_data.mobile_phone)
        self.change_field_value("work", address_data.work_phone)
        self.change_field_value("email", address_data.email_1)
        self.change_field_value("email2", address_data.email_2)
        self.change_field_value("homepage", address_data.home_page)

    def delete_first_contact(self):
        wd = self.app.wd
        # submit deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_contact(self, address_data):
        wd = self.app.wd
        # go to edit page
        self.open_home_page()
        # modify first contact
        self.fill_address_form(address_data)
         # submit modification
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()

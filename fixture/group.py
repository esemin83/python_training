from model.group import Group
from model.group_address import Address_data
import re
from selenium.webdriver.support.ui import Select


class GroupHelper:
#####################################################################################################
    # groups metods

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        #wd.implicitly_wait(20)
        self.group_cache = None

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

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("edit")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        # return to group page
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_some_group(self, new_group_data, index):
        wd = self.app.wd
        #self.select_first_group()
        # open modification form
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_some_group(0)

    def select_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()

    def count_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        #wd.implicitly_wait(20)
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_css_selector("input[value= '%s']" % id).click()

    def modify_some_group_by_id(self, new_group_data, id):
        wd = self.app.wd
        #self.select_first_group()
        # open modification form
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

#####################################################################################################
    # contact metods

    contact_cache = None

    def get_contact_rows(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                id = row.find_element_by_name("selected[]").get_attribute("value")
                text_1 = row.find_element_by_css_selector("td:nth-child(3)").text
                text_2 = row.find_element_by_css_selector("td:nth-child(2)").text
                all_phones = row.find_element_by_css_selector("td:nth-child(6)").text
                text_3 = row.find_element_by_css_selector("td:nth-child(4)").text
                text_4 = row.find_element_by_css_selector("td:nth-child(5)").text
                self.contact_cache.append(Address_data(id=id, firstname=text_1, lastname=text_2,
                                                       all_phone_from_home_page=all_phones, address=text_3,
                                                       all_emails=text_4))
        return list(self.contact_cache)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        home_phone = wd.find_element_by_name('home').get_attribute("value")
        mobile_phone = wd.find_element_by_name('mobile').get_attribute("value")
        work_phone = wd.find_element_by_name('work').get_attribute("value")
        fax_phone = wd.find_element_by_name('fax').get_attribute("value")
        address = wd.find_element_by_name('address').text
        email_1 = wd.find_element_by_name('email').get_attribute("value")
        email_2 = wd.find_element_by_name('email2').get_attribute("value")
        return Address_data(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone,
                            mobile_phone=mobile_phone, work_phone=work_phone, fax_phone=fax_phone,
                            address=address, email_1=email_1, email_2=email_2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Address_data(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def add_new_address_form(self, address_data):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_address_form(address_data)
        # submit contact creation
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

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
        self.change_field_value("fax", address_data.fax_phone)
        self.change_field_value("email", address_data.email_1)
        self.change_field_value("email2", address_data.email_2)
        self.change_field_value("homepage", address_data.home_page)

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_some_contact(0)

    def delete_some_contact(self, index):
        wd = self.app.wd
        # submit deletion
        self.open_home_page()
        self.select_some_contact(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.open_home_page()
        self.contact_cache = None

    def select_some_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_contact(self, address_data):
        wd = self.app.wd
        # go to edit page
        self.open_home_page()
        # modify first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_address_form(address_data)
         # submit modification
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def modify_some_contact(self, address_data, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_address_form(address_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector("td:nth-child(8)")[index].click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector("td:nth-child(7)")[index].click()

    def open_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("fdTableSortTrigger")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_some_contact_by_id(self, id):
        wd = self.app.wd
        # submit deletion
        self.open_home_page()
        self.select_some_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.open_home_page()
        self.contact_cache = None

    def select_some_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value= '%s']" % id).click()

    def modify_some_contact_by_id(self, address_data, id):
        wd = self.app.wd
        self.select_some_contact_by_id(id)
        wd.find_element_by_css_selector("td:nth-child(8)").click()
        self.fill_address_form(address_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

########################################################################
    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_contact_by_id(contact_id)
        wd.implicitly_wait(1)
        wd.find_element_by_name("to_group").click()
        wd.implicitly_wait(1)

        #wd.find_element_by_xpath("//form[@id='right']/select//option['%s']" % number).click()

        #wd.find_element_by_xpath("//option[value= '%s']" % group_id).click()
        wd.find_element_by_css_selector("option[value= '%s']" % group_id).click()
        wd.switch_to_alert().accept()

        #wd.find_element_by_id('208')
        wd.implicitly_wait(1)
        wd.find_element_by_name("add").click()
        wd.implicitly_wait(1)
        self.open_home_page()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.open_group_list_to_edit(group_id)
        self.select_some_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.open_home_page()

    def open_group_list_to_edit(self, group_id):
        wd = self.app.wd
        element = wd.find_element_by_name("group")
        select = Select(element)
        select.select_by_value("%s" % group_id)

    def add_contact_to_group_v01(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_contact_by_id(contact_id)
        element = wd.find_element_by_name("to_group")
        select = Select(element)
        select.select_by_value("%s" % group_id)
        wd.find_element_by_name("add").click()
        self.open_home_page()






# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username= "admin", password= "secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name= "test_5", header= "test_5", footer= "test_5"))
        self.submit_group_creation(wd)
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_group_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username= "admin", password= "secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name= "", header= "", footer= ""))
        self.submit_group_creation(wd)
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, wd, group):
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)

    def init_group_creation(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

        def __init__(self):
            self.wd = WebDriver()
            self.wd.implicitly_wait(60)

        def logout(self):
                # logout
                wd = self.wd
                wd.find_element_by_link_text("Logout").click()

        def return_to_group_page(self):
                # return to group page
                wd = self.wd
                wd.find_element_by_link_text("group page").click()

        def create_group(self, group):
                # fill group form
                wd = self.wd
                self.init_group_creation()
                wd.find_element_by_name("group_name").click()
                wd.find_element_by_name("group_name").clear()
                wd.find_element_by_name("group_name").send_keys("%s" % group.name)
                wd.find_element_by_name("group_header").click()
                wd.find_element_by_name("group_header").clear()
                wd.find_element_by_name("group_header").send_keys("%s" % group.header)
                wd.find_element_by_name("group_footer").click()
                wd.find_element_by_name("group_footer").clear()
                wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
                wd.find_element_by_name("submit").click()
                self.return_to_group_page()

        def init_group_creation(self):
                # init group creation
                wd = self.wd
                self.open_groups_page()
                wd.find_element_by_name("new").click()

        def open_groups_page(self):
                # open groups page
                wd = self.wd
                wd.find_element_by_link_text("groups").click()

        def login(self, username, password):
                # login
                wd = self.wd
                self.open_home_page()
                wd.find_element_by_name("user").click()
                wd.find_element_by_name("user").clear()
                wd.find_element_by_name("user").send_keys("%s" % username)
                wd.find_element_by_name("pass").click()
                wd.find_element_by_name("pass").clear()
                wd.find_element_by_name("pass").send_keys("%s" % password)
                wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

        def open_home_page(self):
                # open home page
                wd = self.wd
                wd.get("http://localhost/addressbook/")

        def destroy(self):
                self.wd.quit()
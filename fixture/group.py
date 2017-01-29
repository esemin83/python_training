

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        # fill group form
        wd = self.app.wd
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

from sys import maxsize


class Address_data:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email_1=None, email_2=None, home_page=None,
                 id=None, all_phone_from_home_page=None, all_emails=None, deprecated=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.all_phone_from_home_page = all_phone_from_home_page
        self.email_1 = email_1
        self.email_2 = email_2
        self.all_emails = all_emails
        self.home_page = home_page
        self.id = id
        self.deprecated = deprecated

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.home_phone,
                                                     self.mobile_phone, self.work_phone, self.all_phone_from_home_page,
                                                     self.address, self.all_emails, self.email_1, self.email_2)

    def __eq__(self, other):
        return (self.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname and self.address == other.address \
               and self.all_emails == other.all_emails \
               and self.all_phone_from_home_page == other.all_phone_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

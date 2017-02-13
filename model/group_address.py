from sys import maxsize


class Address_data:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, email_1=None, email_2=None, home_page=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email_1 = email_1
        self.email_2 = email_2
        self.home_page = home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

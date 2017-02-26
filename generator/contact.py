from model.group_address import Address_data
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    numbers = string.digits + " "*2 + "(" + ")" + "-"
    return "".join([random.choice(numbers) for x in range(maxlen)])


def random_mail(domen, maxlen):
    value = string.ascii_letters + string.digits
    return "".join([random.choice(value) for x in range(random.randrange(maxlen))]) + domen


testdata = [
    Address_data(firstname=random_string("firstname", 20), middlename=random_string("", 1),
                 lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                 company=random_string("company", 20), address=random_string("address", 20),
                 home_phone=random_numbers(10), mobile_phone=random_numbers(10), work_phone=random_numbers(10),
                 fax_phone=random_numbers(10), email_1=random_mail("@mail.ru", 10), email_2=random_mail("@mail.ru", 10),
                 home_page=random_string("page", 15))
    for x in range(n)
]


constant = [
    Address_data(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                 company="company", address="address", home_phone="7874177", mobile_phone="784541212",
                 work_phone="8776464321", fax_phone="874845421", email_1="321@mail.ru", email_2="123@mail.ru",
                 home_page="www.page.com")
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

#with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

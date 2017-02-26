from model.group import Group
import random
import string


constant = [
    Group(name="name_1", header="header_1", footer="footer_1"),
    Group(name="name_2", header="header_2", footer="footer_2")

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*7
    return prefix + "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])

'''
testdata = [Group(name="", header="", footer="")] + \
           [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 15)]
    for header in ["", random_string("header", 15)]
    for footer in ["", random_string("footer", 15)]
]
'''

testdata = [
    Group(name="name_1", header="header_1", footer="footer_1"),
    Group(name="name_2", header="header_2", footer="footer_2")
]
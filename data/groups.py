from common.data_generator import random_string
from model.group import Group

data = [
    Group(name=name, header=header, footer=footer)
    for name in [None, random_string(prefix='name')]
    for header in [None, random_string(prefix='header')]
    for footer in [None, random_string(prefix='footer')]
    ]

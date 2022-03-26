# -*- coding: utf-8 -*-

from common.data_generator import random_email, random_string, random_phone_number
from model.сontact import Contact

data = [Contact(firstname=firstname, middlename=random_string(prefix='middlename'), lastname=lastname, address=address,
                 homephone=random_phone_number(), email=random_email())
            for firstname in [None, random_string(prefix='firstname')]
            for lastname in [None, random_string(prefix='lastname')]
            for address in [None, random_string(prefix='address')]
            ]

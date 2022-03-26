import argparse
import jsonpickle
import os.path

from common.data_generator import random_string, random_phone_number, random_email
from model.сontact import Contact

parser = argparse.ArgumentParser(description='Parse parametres for group generator')
parser.add_argument('-n', action='store', type=int,
                    help='count of generated groups', default=10)
parser.add_argument('-f', action='store', type=str,
                    help='count of generated groups', default="data/contacts.json")
args = parser.parse_args()

contacts = [Contact(firstname=random_string(prefix='firstname'),
                    middlename=random_string(prefix='middlename'),
                    lastname=random_string(prefix='lastname'),
                    address=random_string(prefix='address'),
                    homephone=random_phone_number(),
                    email=random_email())
            for _ in range(args.n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", args.f)
with open(file, 'w') as f:
    jsonpickle.set_encoder_options('json', indent=2)
    f.write(jsonpickle.encode(contacts))

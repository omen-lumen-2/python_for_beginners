import argparse
import jsonpickle
import os.path

from common.data_generator import random_string
from model.group import Group

parser = argparse.ArgumentParser(description='Parse parametres for group generator')
parser.add_argument('-n', action='store', type=int,
                    help='count of generated groups', default=10)
parser.add_argument('-f', action='store', type=str,
                    help='count of generated groups', default="data/groups.json")
args = parser.parse_args()

groups = [
    Group(name=random_string(prefix='name'), header=random_string(prefix='header'), footer=random_string(prefix='footer'))
    for _ in range(args.n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", args.f)
with open(file, 'w') as f:
    jsonpickle.set_encoder_options('json', indent=2)
    f.write(jsonpickle.encode(groups))

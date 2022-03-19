import string
from random import randint, choice, randrange


def random_phone_number():
    prefix = ['+7', '8']
    code_operator = [str(randint(900, 999)), f"({randint(900, 999)})"]
    raw_body = str(randint(10000000, 19999999))[1:]
    body = [raw_body, f"{raw_body[:3]}-{raw_body[3:5]}-{raw_body[5:]}"]
    return f"{choice(prefix)}{choice(code_operator)}{choice(body)}"


def random_email():
    return f"test{randint(1,1000)}@test.test"


def random_int(start=1, end=100):
    return randint(start, end)


def random_string(prefix, maxlen=4):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([choice(symbols) for i in range(randrange(maxlen))])

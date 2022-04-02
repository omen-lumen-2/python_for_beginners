import re
from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 email=None, email2=None, email3=None, all_email_address=None, all_phones=None, group_id=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address  # именно он отображается на главной странице
        # phone
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        # email
        self.email = email
        self.email2 = email2
        self.email3 = email3
        # accumulate variable
        self.all_email_address = all_email_address
        self.all_phones = all_phones
        # group
        self.group_id = group_id

    def __repr__(self):
        return f"id:{self.id}, firstname:{self.firstname}, middlename:{self.middlename}, lastname:{self.lastname}, " \
               f"address:{self.address}, email:{self.email}, email2:{self.email2}, email3:{self.email3}, " \
               f"all_email_address:{self.all_email_address}, all_phones:{self.all_phones}"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        equal_firstname = self.firstname == other.firstname or (self.firstname == None and other.firstname =='') or\
                          (self.firstname == "" and other.firstname ==None)
        equal_lastname = self.lastname == other.lastname or (self.lastname == None and other.lastname == '') or \
                          (self.lastname == "" and other.lastname == None)
        equal_address = self.address == other.address or (self.address == None and other.address == '') or \
                          (self.address == "" and other.address == None)
        equal_id = self.id == None or other.id == None or self.id == other.id

        return equal_address and equal_firstname and equal_lastname and equal_id

    def id_or_max(self):
        return int(self.id) if self.id else maxsize

    def merge_phone(self):
        raw_phones=[self.homephone, self.mobilephone, self.workphone, self.secondaryphone]
        phones = list(filter(lambda x: x != '',
                             map(self.clear_number_phone, filter(lambda x: x is not None, raw_phones))))
        if phones == []:
            return ''
        return '\n'.join(phones)

    def merge_email(self):
        raw_email=[self.email, self.email2, self.email3]
        emails = list(filter(lambda x: x is not None and x != '', raw_email))
        if emails == []:
            return ''
        return '\n'.join(emails)

    @staticmethod
    def clear_number_phone(number):
        return re.sub(r'[-() ]','', number)
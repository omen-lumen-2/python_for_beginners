from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.email = email
        self.id = id

    def __repr__(self):
        return f"id:{self.id},firstname:{self.firstname}, lastname:{self.lastname}, middlename:{self.middlename},\
         email:{self.email}"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return (self.id is None or other.id == None or self.id == other.id) and self.firstname == other.firstname\
               and self.lastname == other.lastname

    def id_or_max(self):
        return int(self.id) if self.id else maxsize

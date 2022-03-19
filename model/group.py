from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return f"id:{self.id},name:{self.name}, header:{self.header}, footer:{self.footer}"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        equal_id = self.id == None or other.id == None or self.id == other.id
        equal_name = self.name == other.name or (self.name == None and other.name == '') or \
                         (self.name == "" and other.name == None)
        return equal_id and equal_name

    def id_or_max(self):
        return int(self.id) if self.id else maxsize

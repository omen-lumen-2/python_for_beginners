from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return f"id:{self.id},name:{self.name}"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return (self.id == None or other.id == None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        return int(self.id) if self.id else maxsize

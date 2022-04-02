import pymysql

from model.group import Group
from model.сontact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=name,
                                          autocommit=True
                                          )

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                list.append(Group(id=str(id), name=name, header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""select id, firstname, lastname, address, email, email2, email3, home, work, mobile, phone2
              from addressbook""")
            for row in cursor:
                id, firstname, lastname, address, email, email2, email3, home, work, mobile, phone2 = row
                list.append(Contact(id=str(id),
                                    firstname=firstname,
                                    lastname=lastname,
                                    address=address,
                                    email=email,
                                    email2=email2,
                                    email3=email3,
                                    homephone=home,
                                    workphone=work,
                                    mobilephone=mobile,
                                    secondaryphone=phone2
                            ))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

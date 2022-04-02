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
        list_group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                list_group.append(Group(id=str(id), name=name, header=header,footer=footer))
        finally:
            cursor.close()
        return list_group

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

    def get_group_of_contact(self, contact_id):
        result = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""SELECT group_id FROM address_in_groups WHERE id={contact_id}""")
            result = cursor.fetchone()
        finally:
            cursor.close()
        return str(result[0])

    def get_contacts_id_with_group(self):
        cursor = self.connection.cursor()
        try:
            # из таблицы не удаляются сущности с удаленными контактами
            cursor.execute("SELECT id FROM address_in_groups WHERE id IN (SELECT id FROM addressbook)")
            result = cursor.fetchall()
        finally:
            cursor.close()
        return [i[0] for i in result]

    def get_last_create_contact_id(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select max(id) from addressbook")
            result = cursor.fetchone()
        finally:
            cursor.close()
        return result[0]

    def destroy(self):
        self.connection.close()

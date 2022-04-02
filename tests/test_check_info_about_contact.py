import random


def test_equal_info_on_home_and_edit_contact_page(app, db):
    app.contact.contact_must_exist(db.get_contact_list())
    index = random.randrange(app.contact.get_count_contact())
    contact_from_home_page = app.contact.get_contact_info_from_home_page(index=index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=index)
    # сравниваем часть параметров
    assert contact_from_home_page == contact_from_edit_page
    # сравниваем телефоны и адресса почты через обратные проверки
    assert contact_from_home_page.all_phones == contact_from_edit_page.merge_phone()
    assert contact_from_home_page.all_email_address == contact_from_edit_page.merge_email()


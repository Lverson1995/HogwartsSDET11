from selenium.webdriver.common.by import By

from homework20200209.page.contact_page import Contact


class TestContact:
    def setup(self):
        self.contact = Contact(reuse=True)


    #作业2  添加用户
    def test_add_user(self):
        self.contact.goto_add_member().add_member("xxx")

    #作业2  编辑用户
    def test_edit_user(self):
        self.contact.edit_member("yangyangyang","yangyangyang1")
